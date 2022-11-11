function solution(s) {
    let answer = s;
    let english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

    english.forEach((arr, i) => {
        answer = answer.split(arr).join(i)
    })
    return Number(answer);
}