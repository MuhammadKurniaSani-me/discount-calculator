Here is the **complete, updated `README.md**`.

I have interpreted "all the docs" to mean you want **Technical Documentation** included in the README. This is excellent for a portfolio because it explains *how* your code solves the specific problems (like handling the dots in currency).

Copy the code block below and overwrite your existing `README.md`.

```markdown
# Discount Calculator App 🇮🇩

A clean, single-page Flask application designed to calculate discounts with Indonesian Rupiah (IDR) formatting.

## 🚀 Features

* **Real-time Input Masking:** Automatically formats numbers with dots as you type (e.g., `100000` → `100.000`).
* **Backend Validation:** Python securely handles the math by stripping formatting before calculation.
* **Indonesian Currency Format:** Results are displayed in the standard IDR format (e.g., `Rp. 15.000`).
* **Error Proof:** Robust error handling for non-numeric inputs.

## 📂 Project Structure

```text
discount-calculator/
│
├── app.py                # Backend: Flask routes & logic
├── requirements.txt      # Dependencies list
├── static/
│   └── style.css         # Styling (Desktop-app look)
└── templates/
    └── index.html        # Frontend: HTML + JavaScript logic

```

## 📖 Technical Documentation

### 1. The Frontend Logic (`index.html`)

We use a custom JavaScript function `formatCurrency(input)` to handle user input.

* **Event Listener:** The `onkeyup` event triggers every time the user types.
* **Regex Processing:**
* `replace(/\./g, '')`: Removes existing dots to get the raw number.
* `replace(/\B(?=(\d{3})+(?!\d))/g, ".")`: Inserts a dot every 3 digits.


* **Benefit:** This creates a smooth user experience where the currency formatting happens instantly.

### 2. The Backend Logic (`app.py`)

Flask receives the data as a formatted string (e.g., "100.000").

* **Sanitization:** `raw_price.replace('.', '')` removes the dots so Python treats it as a standard integer (`100000`).
* **Calculation:**
```python
savings = (price * discount) / 100
final_price = price - savings

```


* **Response:** We send the data back using Jinja2 templating, re-applying the dot format (`.replace(",", ".")`) for the final display.

## 🛠️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone [https://github.com/YOUR_USERNAME/discount-calculator.git](https://github.com/YOUR_USERNAME/discount-calculator.git)
cd discount-calculator

```

### 2. Create and Activate Virtual Environment

* **macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```


* **Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate

```



### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the App

```bash
python app.py

```

Open your browser and visit: `http://127.0.0.1:5000/`

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License.

```

---

### **Don't forget the `requirements.txt`!**
Since the README mentions `pip install -r requirements.txt`, you need to create that file in your project folder.

1.  Run this command in your terminal (inside the project folder):
    ```bash
    pip freeze > requirements.txt
    ```
    *(This takes all the libraries you installed, like Flask, and lists them in a text file).*

2.  Now you can run the git commands to push these changes:
    ```bash
    git add .
    git commit -m "Update README with technical docs"
    git push
    ```

```