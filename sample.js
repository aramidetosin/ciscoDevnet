myObj = {"People":
[
          {
            "id": 1,
            "Firstname": "Aramide",
            "LastName": "Oluwatosin",
            "Email": "aoluwatosin@gmail.com",
            "Active": true
          },
          {
            "id": 2,
            "Firstname": "Aramide",
            "LastName": "Dami",
            "Email": "dfamuyibo@gmail.com",
            "Active": false
          },
          {
          "id": 3,
          "Name": {"FN": "Dayo", "LN": "Aramide"},
          "Email": ["aramide_tosin@yahoo.com", "aramideo@amazon.com"],
          "Active": true
          }
]}

console.log(myObj.People[1].LastName);
console.log(typeof myObj.People[1].Active)
console.log(myObj.People[2].Email[1])