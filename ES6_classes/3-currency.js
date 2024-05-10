export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') throw TypeError('name must be a String');
    if (typeof name !== 'string') throw TypeError('name must be a String');
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(NewCode) {
    if (typeof NewCode !== 'string') {
      throw new TypeError('name must be a String');
    }
    this._code = NewCode;
  }

  get name() {
    return this._name;
  }

  set name(NewName) {
    if (typeof NewName !== 'string') {
      throw new TypeError('name must be a String');
    }
    this._name = NewName;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
