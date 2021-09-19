import json

mintTotal = 3 # your max mint number
i=0
for i in range(mintTotal):

    aDict = {
    "name": "Test #%d" % i,
    "symbol": "",
    "seller_fee_basis_points": 500,
    "image": "0.png",
    "properties": {
      "category": "image",
      "files": [
        {
          "uri": "%d.png" % i,
          "type": "image/png"
        }
      ],
      "creators": [
        {
          "address": "",
          "share": 100
        }
      ]
    },
    
  }
    
    
    jsonString = json.dumps(aDict, indent=3)
    jsonFile = open("%d.json" % i, "w")
    jsonFile.write(jsonString)
    jsonFile.close()
