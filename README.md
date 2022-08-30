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

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

# execute
```bash
curl -s -i http://localhost:5000/dolar
```

```
HTTP/1.1 200 OK
date: Tue, 00 Aug 2022 18:01:52 GMT
server: uvicorn
content-length: 52
content-type: application/json

{
"Compra Dolar":"RD$00.00",
"Venta Dolar":"RD$00.00"
}
```

# License
[MIT](https://choosealicense.com/licenses/mit/)
