let arr1 = [2, 4, 6, 8, 10]
let arr2 = [12, 14, 16, 18, 20]

// arr1 = [-1, 5, 10, 20, 28, 3]
// arr2 = [26, 134, 135, 15, 17]

console.log(smallestDiff(arr1, arr2))

function smallestDiff(array1, array2) {

    array1.sort(function (a, b) { return a - b })
    array2.sort(function (a, b) { return a - b })
    let resultArray = [];
    let smallDiff = Math.abs(array1[0] - array2[0]);
    let currentDiff = Math.abs(array1[0] - array2[0]);
    let i = 0;
    let j = 0;
    while (i < array1.length && j < array2.length) {

        if (array1[i] < array2[j]) {
            currentDiff = Math.abs(array1[i] - array2[j])
            console.log('first if arr1', array1[i])
            console.log('first if arr2', array2[j])
            console.log('first currentDiff', currentDiff)
            i++;
        } else if (array1[i] > array2[j]) {
            currentDiff = Math.abs(array1[i] - array2[j])
            console.log('second if arr1', array1[i])
            console.log('second if arr2', array2[j])
            console.log('second if currentDiff', currentDiff)
            j++;
        } else {
            console.log('else arr1', array1[i])
            console.log('else arr2', array2[j])
            console.log('else currentDiff', currentDiff)

            return [array1[i], array2[j]]
        }
        console.log('after if arr1', array1[i])
        console.log('after if arr2', array2[j])
        console.log('after if currentDiff', currentDiff)
        if (smallDiff > currentDiff) {
            smallDiff = currentDiff;
            resultArray = ([array1[i], array2[j]])

        }

    }
    return resultArray;
}

