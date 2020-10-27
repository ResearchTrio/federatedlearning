# Federated Learning
We here implement the Federated Deep Learning architecture to demonstrate the smart doorbell functionality.  
   It is an attempt to mimic the scenario described in the paper [A Demonstration of Smart Doorbell Design Using FederatedDeep Learning](https://arxiv.org/pdf/2010.09687.pdf).  
   
   **Requirements**
   * Python 3.7
   * tensorflow
   * keras
   * matplotlib
   * Scikit-learn
   * OpenCV
   * Flask
   * Gunicorn
   
   ***
   
   ## Image Dataset Directory Structure  
   ![Dataset directory structure](https://github.com/ResearchTrio/federatedlearning/blob/main/dataset_directory1.png)  
   ***
   
   ## Run the system using the steps below:  
   ### Booting Up
   1. Run Device 1 using
   ```
   gunicorn ---bind localhost:8001 --timeout 600 wsgi1:app
   ```
   2. Run Device 2 using
   ```
   gunicorn ---bind localhost:8002 --timeout 600 wsgi2:app
   ```
   3. Run Main Server using
   ```
   gunicorn ---bind localhost:8000 --timeout 600 wsgi3:app
   ```
