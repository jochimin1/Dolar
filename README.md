# Dolar

Scrape Dolar Price.

## Installation

# clone repo
```bash
git clone https://github.com/jochimin1/Dolar/
```

# change directory
```bash
cd Dolar/
```
# install requirements
```bash
pip install -r requirements.txt
```
# Usage

```uvicorn main:app --reload --host 0.0.0.0 --port 5000```

# execute
```curl -s -i http://localhost:5000/dolar```
```
HTTP/1.1 200 OK
date: Tue, 30 Aug 2022 18:01:52 GMT
server: uvicorn
content-length: 52
content-type: application/json

{
"Compra Dolar":"RD$52.92",
"Venta Dolar":"RD$53.39"
}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
