function solution(numbers) {
    let answer = [];

    for(let i = 0; i < numbers.length; i++){
        for(let j = i+1; j < numbers.length; j++){
            answer.push(numbers[i] + numbers[j])
        }
    }
    return answer.filter((ele, index) => answer.indexOf(ele) === index).sort((a, b) => a - b);
}

// Set이 속도 측면에서 더 좋음
function solution2(numbers) {
    let answer = [];

    for(let i = 0; i < numbers.length; i++){
        for(let j = i+1; j < numbers.length; j++){
            answer.push(numbers[i] + numbers[j])
        }
    }

    answer = [...new Set(answer)].sort((a,b) => a-b)
    return answer
}