# NASA-Space App Challenge-Ontologies and Interactive Network Visualizations 

## Description
<hr>
We developed a network visualization , to find relationship between disparate nasa datasets using metadata described in data.json using ML approaches Embedding, KNN and bm25. We also classified the datasets into 11 classes and 75 sub classes. We have also provided visualization tools to show the above.Also even it can do semantic search as well as keyword search.

## Future Scope
<hr>

### Hybrid engines :  
  Engine Which can work with both Knn and bm25 engine that would allow us to make semantic and keyword search simultenously.

### Better Visualization:
   We can customize D3 to our specific need in which we will be able to load more data in graph as same time
 
### Optimization:
  Currently graph engine takes ~3-4 sec to query and load the page which can be optimized using service workers
 
### Better Training for Cateorgy:
  We can improvise classification with some corretly labeled data. Currently we are using unsupervised Learning to classify the data 
  and search as well.

### Shreding Json:
   we can shred our main data frame into smaller chunks that will help in optimizing engines and serving pages faster 

## Images
<hr>

![image](https://user-images.githubusercontent.com/65333231/135801784-36996b4a-a24e-4d51-8bcc-022a45bd94a0.png)
![image](https://user-images.githubusercontent.com/65333231/135801789-ffd712c0-88f4-4977-adc3-d5d33960e15a.png)
![image](https://user-images.githubusercontent.com/65333231/135801793-30524b73-3c7f-4622-b0a7-bb1e43a2d446.png)
![image](https://user-images.githubusercontent.com/65333231/135802506-3bc0aaf7-c437-4c30-98be-8aac37c76fb5.png)

## Prerequisites
<hr>

Project is based on python Flask framework and D3 for graph genration with help of basic ML

pip install rank_bm25 nltk gensim flask numpy json pickle re 

## Installation  
<hr>

__look into notes to run engine properly__<br>
To install and start server follow the following instructions :  
`git clone https://github.com/Hitansh159/nasa-ontology.git`  
<br>
`cd nasa-ontology`  
<br>
For Bash  
```bash
export FLASK_APP=app
flask run
```  
<br>
For CMD<br>

```
set FLASK_APP=app
flask run
```  

Go to your link localhost:5000

## Contributing
<hr>

Issue Tracking : https://github.com/Hitansh159/nasa-ontology/issues

Note
Due to large size of json they have been put in drive 
download them and put it in `storage` folder
Link: [Drive link](https://drive.google.com/drive/folders/1mAIdQxHOawEoILkSXuyd3VWTdScaAUmb?usp=sharing)

