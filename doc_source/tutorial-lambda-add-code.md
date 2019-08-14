# Step 3: Add Code to the Function<a name="tutorial-lambda-add-code"></a>

\(Previous step: [Step 2: Create the Lambda Function and API](tutorial-lambda-create-function.md)\)

In this step, you replace the starter code for the generated function with specific code that returns information about the day or time you specify\.

With the `index.js` file already open in the editor, completely replace the file's contents with the following code, and then save the file\.

```
'use strict';

exports.handler = function(event, context, callback) {

  if (event.body) {
    event = JSON.parse(event.body);
  }

  var sc; // Status code
  var result = ""; // Response payload

  switch(event.option) {
    case "date":
      switch(event.period) {
        case "yesterday":
          result = setDateResult("yesterday");
          sc = 200;
          break;
        case "today":
          result = setDateResult();
          sc = 200;
          break;
        case "tomorrow":
          result = setDateResult("tomorrow");
          sc = 200;
          break;
        default:
          result = {
            "error": "Must specify 'yesterday', 'today', or 'tomorrow'."
          };
          sc = 400;
          break;
      }
      break;
      case "time":
        var d = new Date();
        var h = d.getHours();
        var mi = d.getMinutes();
        var s = d.getSeconds();

        result = {
          "hour": h,
          "minute": mi,
          "second": s
        };
        sc = 200;
        break;
      default:
        result = {
          "error": "Must specify 'date' or 'time'."
        };
        sc = 400;
      break;
  }

  const response = {
    statusCode: sc,
    headers: { "Content-type": "application/json" },
    body: JSON.stringify( result )
  };

  callback(null, response);

  function setDateResult(option) {

    var d = new Date(); // Today
    var mo; // Month
    var da; // Day
    var y; // Year

    switch(option) {
      case "yesterday":
        d.setDate(d.getDate() - 1);
        break;
      case "tomorrow":
        d.setDate(d.getDate() + 1);
      default:
       break;
    }

    mo = d.getMonth() + 1; // Months are zero offset (0-11)
    da = d.getDate();
    y = d.getFullYear();

    result = {
      "month": mo,
      "day": da,
      "year": y
    };

    return result;
  }
};
```

This function takes an incoming payload with an `option` value of `date` or `time`\. If `date` is specified, you must also specify a `period` value of `yesterday`, `today`, or `tomorrow`\. The function then returns the corresponding `month`, `day`, and `year`\. If, however, an `option` value of `time` is specified, the function returns the current `hour`, `minute`, and `second`\.

## Next Step<a name="tutorial-lambda-add-code-next"></a>

[Step 4: Run or Debug the Function Locally](tutorial-lambda-run-or-debug-local-function.md)