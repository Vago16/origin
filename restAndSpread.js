///* Write an ES2015 Version */
const filterOutOdds = (...args) => args.filter(num % 2 ===0);

const findMin = (...nums) => Math.min(...nums);

const mergeObjects = (thing1, thing2) => ({...thing1, ...thing2});

const doubleAndReturnArgs = (arr, ...args)=> [...arr, ...args(val => cal * 2)];

const removeRandom = (items) => {
    let index = Math.floor(Math.random() * items.length);
    return [...items.slice(0, index), ...items.slice(index + 1)];
};

const extend = (array1, array2) => {
    return [...array1, ...array2];
};

const addKeyVal = (obj, key, val) => {
    let newObj = {...obj}
    newObj[key] = val;
    return newObj;
};

const removeKey = (obj, key) => {
    let newObj = { ...obj }
    delete newObj[key]
    return newObj;
};

const combine = (obj1, obj2) => {
    return { ...obj1, ...obj2 };
  };

  const update = (obj, key, val) => {
    let newObj = {...obj}
    newObj[key] = val;
    return newObj;
  };

