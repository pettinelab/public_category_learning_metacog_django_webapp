


/* functions */
function linspace(start, stop, num) {
    const step = (stop - start) / (num - 1);
    const arr = new Array(num).fill().map((_, i) => {
        return start + i * step;
    });
    return arr;
    }


function binEstimatesOutcomes(estimates,outcomes) {
    counts = Array.apply(null, Array(confidence_keys.length)).map(function () {return 0;})
    correct = Array.apply(null, Array(confidence_keys.length)).map(function () {return 0;})
    for (let i = 0; i < estimates.length; i++) {
        counts[estimates[i]-1]++;
        correct[estimates[i]-1] += outcomes[i]
    }
    var estimates_binned_ = linspace(.5, 1, confidence_keys.length+1);
    var estimates_binned = Array.apply(null, Array(estimates_binned_.length-1)).map(function (x, i) 
        {return(estimates_binned_[i]+estimates_binned_[i+1])/2});
    var outcomes_binned = correct.map(function(n, i) { return n / counts[i]; }).map((value) => {
        return isNaN(value) ? 0 : value;});
    return [estimates_binned, outcomes_binned, counts];
}


function calcCalibration(estimates_binned, outcomes_binned, counts){
    calibration = Array.apply(null, Array(confidence_keys.length))
        .map(function (x, i) { 
        return counts[i]*((estimates_binned[i]-outcomes_binned[i])**2)})
        .reduce((a,b) => a + b, 0) / 
        counts.reduce((partialSum, a) => partialSum + a, 0);

return calibration;
}


function convertCalibration(estimates_binned,outcomes_binned, counts){
    var estimates_binned_worst = estimates_binned.map(val => Math.min((val<0.75)+.5,1));
    var counts_random = Array.apply(null, Array(estimates_binned.length)).map(function () {return 1;});
    var calibration_worst = calcCalibration(estimates_binned, estimates_binned_worst, counts_random);
    var calibration = calcCalibration(estimates_binned, outcomes_binned, counts);
    var calibration_converted_score = 1 - (calibration / calibration_worst);
    calibration_converted_score = Math.min(calibration_converted_score, 1)
    return calibration_converted_score
}

function scoreCalibration(estimates,outcomes) {
    [estimates_binned, outcomes_binned, counts] = binEstimatesOutcomes(estimates,outcomes)
    var calibration_converted_score = convertCalibration(estimates_binned,outcomes_binned, counts)
    return calibration_converted_score
}

function blockFeedbackMessage(block){
    var trials_categorize = jsPsych.data.get().filter({task: 'classification', block: block});
    var correct_by_trial = trials_categorize.trials.map(trial => Number(trial.correct));
    var correct_trials = trials_categorize.filter({correct: true});
    var accuracy = Math.round(correct_trials.count() / trials_categorize.count() * 100);
    var trials_confidence = jsPsych.data.get().filter({task: 'confidence', block: block});
    var confidence_ratings = trials_confidence.trials.map(trial => parseInt(trial.response));
    var calibration_score = Math.round(scoreCalibration(confidence_ratings,correct_by_trial)*100);

    var message =  `<p>You responded correctly on ${accuracy}% of the samples.</p>
        <p>Your judgement calibration score was was ${calibration_score}.</p>
        <p>The joint score was ${(accuracy+calibration_score)/2}</p>
        <p>Press any key to continue.</p>`;

    return message
}