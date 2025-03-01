/* eslint-disable */
import Currency from './3-currency.js';

class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') throw TypeError('Amount must be a number');
    if (!(currency instanceof Currency)) throw TypeError('Currency must be an instance of Currency');
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }
  set amount(value) {
    if (typeof value !== 'number') throw TypeError('Amount must be a number');
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }
  set currency(value) {
    if (!(value instanceof Currency)) throw TypeError('Currency must be an instance of Currency');
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw TypeError('Amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}

export default Pricing;