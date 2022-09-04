# OFH2022 VeggieBox


### Tools
* https://dash.plotly.com/installation


### Ansichten
* 40 graph lines (y) for each kw (x) ✔
* local availability vs production for blumenkohl ✔


### Process Steps
1. execute create-files.py
2. copy from xlsx to kwX.txt
3. execute text-transform.py
4. copy from terminal to data.json

### Deployment
* `docker build -t ofh2022-veggiebox:0.1 .\ `
* `docker tag ofh2022-veggiebox:0.1 io42630/ofh2022-veggiebox:0.1`
* `docker push io42630/ofh2022-veggiebox:0.1`
* 




