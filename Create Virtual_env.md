# Setting Up and Activating a Virtual Environment

This guide explains how to create and activate a virtual environment for Python 3.9 or 3.11 using either Conda or Python's built-in `venv` module.

---

## **Using Conda**

### 1. **Create a Conda Environment**
   Run the following command to create a Conda environment with Python 3.9 or 3.11:
   ```bash
   conda create --name <env_name> python=3.11
   ```
   Replace `<env_name>` with the name of your environment (e.g., `quantum_sim).

### 2. **Activate the Conda Environment**
   To activate the environment, use:
   ```bash
   conda activate <env_name>
   ```

### 3. **Deactivate the Conda Environment**
   To deactivate the environment, use:
   ```bash
   conda deactivate
   ```

---

## **Using Python's Built-in `venv`**

### 1. **Create a Virtual Environment**
   Run the following command to create a virtual environment:
   ```bash
   python -m venv <env_name>
   ```
   Replace `<env_name>` with the name of your virtual environment (e.g., `venv`).

### 2. **Activate the Virtual Environment**
   - **On Windows**:
     ```bash
     <env_name>\Scripts\activate
     ```
   - **On Linux/Mac**:
     ```bash
     source <env_name>/bin/activate
     ```

### 3. **Deactivate the Virtual Environment**
   To deactivate the virtual environment, use:
   ```bash
   deactivate
   ```

---

## **Verify the Python Version**
After activating the environment, verify the Python version to ensure it matches your desired version (e.g., 3.9 or 3.11):
```bash
python --version
```

---

## **Install Dependencies**
Once the environment is activated, install the required dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Additional Notes**
- Always activate the environment before running your Python scripts.
- Use `pip freeze > requirements.txt` to save the current environment's dependencies.

Let me know if you need further assistance!
