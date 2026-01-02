from flask import Flask, render_template, request

app = Flask(__name__)

# --- The Simple Function You Requested ---
def calculate_final_price(original_price, discount_percent):
    """Calculates the final price after discount."""
    savings = (original_price * discount_percent) / 100
    final_price = original_price - savings
    return final_price, savings

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            # 1. Get the raw text (e.g., "100.000")
            raw_price = request.form.get('price')
            
            # 2. CLEAN IT: Remove the dots so Python sees "100000"
            clean_price = raw_price.replace('.', '')
            
            # 3. Convert to float
            price = float(clean_price)
            discount = float(request.form.get('discount'))

            # 4. Calculate
            final, saved = calculate_final_price(price, discount)

            # 5. Format results with DOTS for Indonesian style
            # We use {:,.0f} to get commas, then swap commas to dots
            result = {
                'original': f"{price:,.0f}".replace(",", "."),
                'discount': f"{discount}",
                'saved': f"{saved:,.0f}".replace(",", "."),
                'final': f"{final:,.0f}".replace(",", ".")
            }
        except ValueError:
            error = "Please enter valid numbers only."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)