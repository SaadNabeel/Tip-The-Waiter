def totalcalc(billamount, tipperc):
    tipamount = (tipperc / 100) * billamount  
    totalamount = billamount + tipamount      
    print("Bill Amount: $", "{billamount:,.2f},",
          "Tip Percentage:", "{tipperc}%,",
          "Tip Amount: $", "{tipamount:,.2f},",
          "Total Amount to Pay: $", f"{totalamount:,.2f}")

# Example usage:
totalcalc(100, 15)
