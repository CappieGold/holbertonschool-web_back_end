import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// ---------- Data ----------
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((p) => p.id === Number(id));
}

// ---------- Redis (callbacks -> promisify) ----------
const client = redis.createClient();
client.on('error', (err) => {
  console.error(`Redis error: ${err.message}`);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function reserveStockById(itemId, stock) {
  const key = `item.${itemId}`;
  return setAsync(key, stock);
}

async function getCurrentReservedStockById(itemId) {
  const key = `item.${itemId}`;
  const val = await getAsync(key);
  return val === null ? 0 : Number(val);
}

// ---------- Express ----------
const app = express();
const PORT = 1245;

app.get('/list_products', (_req, res) => {
  const payload = listProducts.map((p) => ({
    itemId: p.id,
    itemName: p.name,
    price: p.price,
    initialAvailableQuantity: p.stock,
  }));
  res.json(payload);
});

app.get('/list_products/:itemId', async (req, res) => {
  const product = getItemById(req.params.itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const reserved = await getCurrentReservedStockById(product.id);
  const currentQuantity = Math.max(product.stock - reserved, 0);

  return res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const product = getItemById(req.params.itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const reserved = await getCurrentReservedStockById(product.id);
  const available = product.stock - reserved;

  if (available <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: product.id });
  }

  await reserveStockById(product.id, reserved + 1);
  return res.json({ status: 'Reservation confirmed', itemId: product.id });
});

app.listen(PORT, () => {
  console.log(`API listening on port ${PORT}`);
});

export default app;
