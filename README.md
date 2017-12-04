### EasyShopping-Semantic-Web-Application


#### Authors:
1. Pranjal Karankar
2. Pushkar Ladhe
3. Mukulsingh Jadhav
4. Tushar Pandit

#### Technology Stack:
1. Data scraping - Python, Selenium Web Driver
2. Web Development - JavaScript, NodeJS, Express, Bootstrap

#### Application installation steps:

Prerequisites-
- Latest Node.js 8 should be installed which comes NPM
- Downloadable at :	https://nodejs.org/en/

Installation of Fuseki
- Extract the zip file of Apache Fuseki v3.4
- Run the command "java -jar .\fuseki-server.jar" inside the extracted folder
- Create a new dataset named "easyshop" on the fuseki server and upload 3 RDF files
namely Nutrition, Store, and Location. (RDF files are available on the github/attahced here)

Web app :
- Once the RDF files are hosted on the Fuseki server, the web application can be tested using following steps:
- Inside Easy Shop VueJS directory run the following commands:
 	- To install all the dependenies: npm install
	- To run the application: npm run dev
- Application now will be running at http://localhost:8080
