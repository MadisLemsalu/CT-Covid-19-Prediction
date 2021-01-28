# CT-Covid-19-Prediction

Prediction of Covid-19 from CT-scans. The input modality is CT-images directly after conversion to PNG resulted in information loss. The project was done as a consulatancy project to ZGT and therefore most of the code is proprietary. 


If you have a trained model, app.py can be called with REST API: 

**********************************
Instructions to call the server
**********************************


1) cd to app.py

2) run server: python app.py

3) For single image: 

curl -F 'image=@test.dcm' 0.0.0.0:8000/predict


For a folder (replace corads6 with the folder name):

find corads6 -type f -exec curl -F 'image=@{}' 0.0.0.0:8000/predict \;

---

Results will be saved into output.csv where the third column is the algorithm's confidence in covid
