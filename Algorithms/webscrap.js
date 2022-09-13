/*
1.newsapi.org
2.coinapi.io
3.commodities-api.com
4.nist cve api
5.pro public api
6.whitehouse api
7.nonprofit api https://projects.propublica.org/nonprofits/api/v2
8. cik https://data.sec.gov/submissions/CIK##########.json
new york times https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=yourkey

grab and insert into db
 */

const axios = require('axios')

function vulnerabiltiesApi(){
    axios.get('https://services.nvd.nist.gov/rest/json/cves/1.0/')
    .then(res => {console.log(res.data.result.CVE_Items)})
    .catch(err => {console.log("Error")})
}

function commoditiesApi(){
    endpoint = 'latest'
    access_key = ''
    axios.get('https://commodities-api.com/api/' + endpoint + '?access_key=' + access_key)
    .then(res => {console.log(res.data)})
    .catch(err => {console.log("Error")})
}

function newsApi(){
    category = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    access_key = ''
    axios.get(`https://newsapi.org/v2/top-headlines?category=business&language=en&from=2022-09-08&sortBy=popularity&apiKey=${access_key}`)
    .then(res => {console.log(res.data.articles)})
    .catch(err => {console.log("Error")})
}

function cryptoApi(){
    axios.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=')
    .then(res => {console.log(res.data)})
    .catch(err => {console.log(err)})
}

function securityExchangeApi(){
    axios.get('https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent')
    .then(res => {console.log(res.data)})
    .catch(err => {console.log("Error")})

}









function congressApi(){
    axios.get('https://api.propublica.org/congress/v1/PAh2GHkwKSXTAAU8l1lgeBIewQt9vz5ibEiEM9DD',{"X-API-Key":"PAh2GHkwKSXTAAU8l1lgeBIewQt9vz5ibEiEM9DD"})
    .then(res => {console.log(res.data)})
    .catch(err => {console.log("Error")})
}
function none(){
    const options = {
        header: {
            "X-CoinAPI-Key": access_key
        }
      };
      
      axios.get(url, options)
        .then( res => console.log(res.data))
        .then( data => console.log(data) );

    }

function whiteHouseApi(){
    axios.get('')
    .then(res => {console.log(res.data)})
    .catch(err => {console.log("Error")})
}

function nonProfit(){
    axios.get('https://projects.propublica.org/nonprofits/api/v2')
    .then(res => {console.log(res.json())})
    .catch(err => {console.log("Error")})

}

newsApi()