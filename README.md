## 🧪 Setting Up a Virtual Environment

Follow these steps to create and use a Python virtual environment for this project.

---

### 1. Navigate to Your Project Folder

```bash
cd your-project-folder
```


### 2. Create a Virtual Environment
```bash
python -m venv venv
```
**This creates a folder called venv containing an isolated Python environment.**

### 3. Activate the Virtual Environment
```bash
source venv/bin/activate
```

### 4. Confirm Activation

You should see something like:
```text
(venv) your-folder-name $
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```
Or install manually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn mlflow
```

### 6. Save Dependencies (Optional)

```bash
pip freeze > requirements.txt
```

### 7. Deactivate the Environment

```bash
deactivate
```

### 8. Reusing the Environment

```bash
# Activate environment
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

