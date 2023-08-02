const {getMean, getMedian, getMode} = require("./functions");

/**1 Mean Test */
describe("#getMean", function() {
    it("gets the mean for an odd set of numbers in an array", function() {
        expect(getMean([2, 4, 6])).toEqual(3)
        expect(getMean([-2, -4, -6])).toEqual(-3)
    })
    it("gets the mean for an even set of numbers in an array", function(){
        expect(getMean([2, 4, 6, 8])).toEqual(5)
        expect(getMean([-2, -4, -6, -8])).toEqual(-5)
    })
    it("gets the mean for an empty of numbers in an array", function(){
        expect(getMean([])).toEqual(0)
    })
})

/**2 Median Test */
describe("#getMedian", function() {
    it("gets the median for an odd set of numbers in an array", function() {
        expect(getMedian([2, 4, 6])).toEqual(4)
        expect(getMedian([-2, -4, -6])).toEqual(-4)
    })
    it("gets the mean for an even set of numbers in an array", function(){
        expect(getMedian([2, 4, 6, 8])).toEqual(5)
        expect(getMedian([-2, -4, -6, -8])).toEqual(-5)
    })
})

/**3 Mode test */
describe("#getMode", function() {
    it("gets the mode for a set of numbers in an array", function() {
        expect(getMode([0, 1, 1, 1, 2, 3])).toEqual(1)
        expect(getMode([-2, -2, -2])).toEqual(-2)
    })
})