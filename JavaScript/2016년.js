function solution(a, b) {
    let answer = '';

    const day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'];
    const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let date = b-1;

    for(let i = 0; i < a-1; i++){
        date += month[i];
    }

    answer = day[date%7]
    return answer;
}

function solution2(a, b) {
    let answer = '';

    const day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    let date = new Date(`2016-${a}-${b}`);
    answer = date.getDay();

    return day[answer]
}