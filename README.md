# parser_finhub
parser django project inside of docker


 
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    
  </a>


</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This is a django project that uses finhub api to collect data about 5 types of quotes every 15 minutes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Django
* Celery
* Redis
* Docker
* Docker-compose
* Postgresql


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project runs in docker container so all requirements are written in requirements.txt file.  Here is the shor list

 
###  Postgresql
### Docker
### Docker-compose
### redis 
### Python 3.11.1 python-crontab==2.7.1  psycopg2==2.9.6 celery finnhub-python Django==4.1.4
  djangorestframework==3.14.0
  django-cors-headers==4.0.0
  django-celery-results==2.5.1
  django-celery-beat==2.5.0

### Prerequisites

* Have an installed docker and docker-compose on your local machine
 

### Installation


1. Clone the repo
   ```sh
   git clone github.com/batya-o0O/parser_finhub.git
   ```
2. Build the docker images
    ```sh 
   docker-compose build
    ```
3.  Before running the docker container we should make migrations to our database to create table for celery worker results.
    ```sh 
     docker-compose run django python manage.py migrate
    ```
  

4. Run the docker container
    ```sh 
   docker-compose up
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the app inside of the container. The project runs on http://localhost:8000 

You will see recent updates of the quotes. By clicking on it you can see all the records of that quote. The new records appears every 15 minutes.

To use REST api, go the the http://localhost:8000/api/    You can see available api

To get json quotes go to the http://localhost:8000/api/quotes/

By providing name you will get all json object with that name of the quote for example by going to this page http://localhost:8000/api/quotes/AAPL you will obtain all json quotes of AAPL

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Telegram: @batya_o0O

Project Link: [https://github.com/batya-o0O/parser_finhub](https://github.com/batya-o0O/parser_finhub)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<p align="right">(<a href="#readme-top">back to top</a>)</p>





