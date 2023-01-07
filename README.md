# data-warehouse-with-dbt

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">City Traffic Data Warehouse</h3>

  <p align="center">
    A fully dockerized ELT pipeline project, using Airflow, PostgreSQL, DBT, and Redash.
    <br />
   
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Introduction">Introduction</a></li>
        <li><a href="#Objective">Objective</a></li>
        <li><a href="#Data">Data</a></li>
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
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- <p align="center">
     <img src="pipeline2.png">
</p> -->

### Introduction

A city traffic department wants to collect traffic data using swarm UAVs (drones) from a
number of locations in the city and use the data collected for improving traffic flow in the
city and for a number of other undisclosed projects.


### Objective

Create a scalable data warehouse that will host the vehicle trajectory data extracted by
analyzing footage taken by swarm drones and static roadside cameras.
The data warehouse should take into account future needs, organize data such that a
number of downstream projects query the data efficiently. Ue the Extract Load
Transform (ELT) framework using DBT. 

### Data

In this project I have used pNEUMA data.pNEUMA data is open large-scale dataset of naturalistic trajectories of half a million vehicles that have been collected by a one-of-a-kind experiment by a swarm of drones in the congested downtown area of Athens, Greece.


### Built With

Tech Stack used in this project
* [Airflow](https://airflow.apache.org/)
* [PostgreSQL](https://postgresql.com)
* [DBT](https://www.getdbt.com/)
* [Redash](https://redash.io/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo and Navigate
   ```sh
   git clone https://github.com/tibarekb/data-warehouse-with-dbt.git
   cd data-warehouse-with-dbt
   ```
2. Run
   ```sh
    docker-compose -f docker-compose.yaml up --build
   ```


<!-- CONTACT -->
## Contact

Tibarek Berassu - berassut@gmail.com



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [10 Academy](https://www.10academy.org/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tibarekb/data-warehouse-with-dbt.svg?style=for-the-badge
[contributors-url]: https://github.com/tibarekb/Datawarehouse/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tibarekb/data-warehouse-with-dbt.svg?style=for-the-badge
[forks-url]: https://github.com/tibarekb/data-warehouse-with-dbt/network/members
[stars-shield]: https://img.shields.io/github/stars/tibarekb/data-warehouse-with-dbt.svg?style=for-the-badge
[stars-url]: https://github.com/tibarekb/data-warehouse/stargazers
[issues-shield]: https://img.shields.io/github/issues/tibarekb/data-warehouse-with-dbt.svg?style=for-the-badge
[issues-url]: https://github.com/tibarekb/data-warehouse/issues
[license-shield]: https://img.shields.io/github/license/tibarekb/data-warehouse-with-dbt.svg?style=for-the-badge
[license-url]: https://github.com/tibarekb/data-warehosue/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tibarek-mesfin-berassu-309508222
<!-- [product-screenshot]:  -->






