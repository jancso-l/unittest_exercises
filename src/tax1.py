class SimpleTaxCalculator:
    FIRST_THRESH = 17.0
    SECOND_THRESH = 32.0
    THRESHOLD = 85528
    VAT_TAX_RATE = 23.0
    CAPITAL_GAINS_TAX_RATE = 19.0

    def income_tax(self, income):
        first_rate = self.FIRST_THRESH / 100.0
        second_rate = self.SECOND_THRESH / 100.0
        if income < self.THRESHOLD:
            return income * first_rate
        else:
            return self.THRESHOLD * first_rate + (income - self.THRESHOLD) * second_rate

    def vat_tax(self, net_price):
        tax_rate = self.VAT_TAX_RATE / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit):
        tax_rate = self.CAPITAL_GAINS_TAX_RATE / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0
