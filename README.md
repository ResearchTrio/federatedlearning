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
   This will start the Gunicorn servers for Device 1 ,Device 2 and Main Server
   
   ###### Servers:
   * Main Server - ```http://localhost:8000/```
   * Device 1 - ```http://localhost:8001/```
   * Device 2 - ```http://localhost:8002/```
   
   ##### System Working
   1. First a model is trained locally on the device. Click on the ```Model Training (Locally)``` button to start model training. This button will send ```http://localhost:8001/modeltrain``` and ```http://localhost:8002/modeltrain``` requests respectively to train models locally.  
   2. Once the models are trained click on ```Send Model to Federated Server``` button. This will send the client models trained on the local devices to the main server using ```http://localhost:8001/sendmodel``` an ```http://localhost:8001/sendmodel``` requests respectively.
   3. On sending the local models they are stored into the Main Server. Now click on ```Aggregate Local Models``` button that sends ```http://localhost:8000/aggregate_models``` request to start model aggregation of the locally trained models.
   4. Now, once the model aggregation is done click on the ```Send Aggregated Models to Federated Clients``` button that sends ```http://localhost:8000/send_model_clients``` request to send the global aggregated model back to the local devices.
   5. Once the complete iteration is finished go back to step one for the next iteration of model training and aggregation for improving the accuracy of the aggregated model. 
