const express = require('express');
const app = express(); 
const ExpressError = require('./ExpressError');
const {numberCounter, isNum, getMean, getMedian, getMode} = require('./functions')

app.use(express.json());
/**ROUTES */
/**1 Mean Route */
app.get('/mean', function(req, res, next) {
  if (!req.query.nums) {
    throw new ExpressError('Numbers are required to calculate the mean.', 400)
  }
  let susArr = req.query.nums.split(',');
  let nums = isNum(susArr);
  if (nums instanceof Error) {
    throw new ExpressError(nums.message);
  }
  let results = {
    mathFunction: "mean",
    results: getMean(nums)
  }
  return res.send(results);
  })

/**2 Median Route */
app.get('/mean', function(req, res, next) {
  if (!req.query.nums) {
    throw new ExpressError('Numbers are required to calculate the median.', 400)
  }
  let susArr = req.query.nums.split(',');
  let nums = isNum(susArr);
  if (nums instanceof Error) {
    throw new ExpressError(nums.message);
  }
  let results = {
    mathFunction: "median",
    results: getMedian(nums)
  }
  return res.send(results);
})

/**3 Mode Route */
app.get('/mean', function(req, res, next) {
  if (!req.query.nums) {
    throw new ExpressError('Numbers are required to calculate the mode.', 400)
  }
  let susArr = req.query.nums.split(',');
  let nums = isNum(susArr);
  if (nums instanceof Error) {
    throw new ExpressError(nums.message);
  }
  let results = {
    mathFunction: "mode",
    results: getMode(nums)
  }
  return res.send(results);
})

/** blank next() error handler */
app.use(function (req, res, next) {
  const err = new ExpressError("Route not found", 404);
  return next(err);
});
/**500 internal server error handler */
app.use(function (err, req, res, next) {
  res.status(err.status || 500);
  return res.json({
    error: err,
    message:err.message
  });
});
/**app listener */
app.listen(3000, function() {
    console.log(`Server has been started on port 3000`);
  });