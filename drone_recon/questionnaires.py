"""
This file contains dictionarries for several potential questionnaires to be used in the study.

"""

'''
The Obsessive–Compulsive Inventory: Development and Validation of a Short Version
'''

answers = {
    'Not at all': 0,
    'A little': 1,
    'Moderately': 2,
    'A lot': 3,
    'Extremely': 4
}

QUESTIONNAIRE_OCI = {
    'I have saved up so many things that they get in the way.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 1
    },
    'I check things more often than necessary.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 2
    },
    'I get upset if objects are not arranged properly.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 3
    },
    'I feel compelled to count while I am doing things.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 4
    },
    'I find it difficult to touch an object when I know it has been touched by strangers or certain people.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 5
    },
    'I find it difficult to control my own thoughts.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 6
    },
    'I collect things I don’t need.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 7
    },
    'I repeatedly check doors, windows, drawers, etc.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 8
    },
    'I get upset if others change the way I have arranged things.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 9
    },
    'I feel I have to repeat certain numbers.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 10
    },
    'I sometimes have to wash or clean myself simply because I feel contaminated.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 11
    },
    'I am upset by unpleasant thoughts that come into my mind against my will.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 12
    },
    'I avoid throwing things away because I am afraid I might need them later.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 13
    },
    'I repeatedly check gas and water taps and light switches after turning them off.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 14
    },
    'I need things to be arranged in a particular order.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 15
    },
    'I feel that there are good and bad numbers.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 16
    },
    'I wash my hands more often and longer than necessary.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 17
    },
    'I frequently get nasty thoughts and have difficulty in getting rid of them.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 18
    }
}


'''
The Broader Autism Phenotype Questionnaire
'''

answers = {
    'Very rarely': 1,
    'Rarely': 2,
    'Occasionally': 3,
    'Somewhat often': 4,
    'Often': 5,
    'Very often': 6
}

answers_reverse = {}
values = list(answers.values())
values.reverse()
for key, val in zip(answers.keys(),values):
    answers_reverse[key] = val

QUESTIONNAIRE_BAPQ = {
    'I like being around other people.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 1
    },
    'I find it hard to get my words out smoothly': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 2
    },
    'I am comfortable with unexpected changes in plans.': {
        'subscale': 'Rigid',
        'answers': answers_reverse,
        'question_number': 3
    },
    'It’s hard for me to avoid getting sidetracked in conversation.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 4
    },
    'I would rather talk to people to get information than to socialize.': {
        'subscale': 'Aloof',
        'answers': answers,
        'question_number': 5
    },
    'People have to talk me into trying something new.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 6
    },
    'I am ‘‘in-tune’’ with the other person during conversation***.': {
        'subscale': 'Pragmatic Language',
        'answers': answers_reverse,
        'question_number': 7
    },
    'I have to warm myself up to the idea of visiting an unfamiliar place.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 8
    },
    'I enjoy being in social situations.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 9
    },
    'My voice has a flat or monotone sound to it.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 10
    },
    'I feel disconnected or ‘‘out of sync’’ in conversations with others***.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 11
    },
    'People find it easy to approach me***.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 12
    },
    'I feel a strong need for sameness from day to day.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 13
    },
    'People ask me to repeat things I’ve said because they don’t understand.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 14
    },
    'I am flexible about how things should be done.': {
        'subscale': 'Rigid',
        'answers': answers_reverse,
        'question_number': 15
    },
    'I look forward to situations where I can meet new people.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 16
    },
    'I have been told that I talk too much about certain topics.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 17
    },
    'When I make conversation it is just to be polite***.': {
        'subscale': 'Aloof',
        'answers': answers,
        'question_number': 18
    },
    'I look forward to trying new things.': {
        'subscale': 'Rigid',
        'answers': answers_reverse,
        'question_number': 19
    },
    'I speak too loudly or softly.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 20
    },
    'I can tell when someone is not interested in what I am saying***.': {
        'subscale': 'Pragmatic Language',
        'answers': answers_reverse,
        'question_number': 21
    },
    'I have a hard time dealing with changes in my routine.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 22
    },
    'I am good at making small talk***.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 23
    },
    'I act very set in my ways.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 24
    },
    'I feel like I am really connecting with other people.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 25
    },
    'People get frustrated by my unwillingness to bend.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 26
    },
    'Conversation bores me***.': {
        'subscale': 'Aloof',
        'answers': answers,
        'question_number': 27
    },
    'I am warm and friendly in my interactions with others***.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 28
    },
    'I leave long pauses in conversation.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 29
    },
    'I alter my daily routine by trying something different.': {
        'subscale': 'Rigid',
        'answers': answers_reverse,
        'question_number': 30
    },
    'I prefer to be alone rather than with others.': {
        'subscale': 'Aloof',
        'answers': answers,
        'question_number': 31
    },
    'I lose track of my original point when talking to people.': {
        'subscale': 'Pragmatic Language',
        'answers': answers,
        'question_number': 32
    },
    'I like to closely follow a routine while working.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 33
    },
    'I can tell when it is time to change topics in conversation***.': {
        'subscale': 'Pragmatic Language',
        'answers': answers_reverse,
        'question_number': 34
    },
    "When checked if I'm reading questions closely (like now), I select 'often' as my response.": {
        'subscale': 'Attention Check',
        'answers': answers,
        'question_number': 0
    },
    'I keep doing things the way I know, even if another way might be better.': {
        'subscale': 'Rigid',
        'answers': answers,
        'question_number': 35
    },
    'I enjoy chatting with people***.': {
        'subscale': 'Aloof',
        'answers': answers_reverse,
        'question_number': 36
    },
}

"""
Conner's Scales for ADHD - Screener
"""

answers = {
    'Not at all, never': 0,
    'Just a little, once in a while': 1,
    'Pretty much, often': 2,
    'Very much, very frequently': 3
}

QUESTIONNAIRE_CONNERS_SCREEN = {
    'I lose things necessary for tasks or activities (e.g. to-do lists, pencils, books or tools).': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 1
    },
    'I talk too much.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 2
    },
    'I am always on the go, as if driven by a motor.': {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 3
    },
    'I have trouble doing leisure activities quietly.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 4
    },
    'I have a short fuse/hot temper.': {
        'subscale': 'Impulsivity_Emotional Lability,ADHD Index',
        'answers': answers,
        'question_number': 5
    },
    'I leave my seat when I am not supposed to.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 6
    },
    'I still throw tantrums.': {
        'subscale': 'Impulsivity_Emotional Lability,ADHD Index',
        'answers': answers,
        'question_number': 7
    },
    'I have trouble waiting in line or taking turns with others.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 8
    },
    'I have trouble keeping my attention focused when working.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 9
    },
    'I avoid new challenges because I lack faith in my abilities.': {
        'subscale': 'Problems with Self-Concept,ADHD Index',
        'answers': answers,
        'question_number': 10
    },
    'I feel restless inside even if I am sitting still.': {
        'subscale': 'Hyperactivity_Restlessness,ADHD Index',
        'answers': answers,
        'question_number': 11
    },
    "Things I hear or see distract me from what I'm doing.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 12
    },
    'I am forgetful in my daily activities.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 13
    },
    'I have trouble listening to what other people are saying.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 14
    },
    'I am an underachiever.': {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 15
    },
    'I am always on the go.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 16
    },
    "I can't get things done unless there's an absolute deadline.": {
        'subscale': 'Inattention_Memory Problems,ADHD Index',
        'answers': answers,
        'question_number': 17
    },
    'I fidget (with my hands or feet) or squirm in my seat.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 18
    },
    'I make careless mistakes or have trouble paying close attention to detail.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 19
    },
    "I intrude on others' activities": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 20
    },
    "I don't like homework or job activities where I have to think a lot.": {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 21
    },
    'I am restless or overactive.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 22
    },
    "Sometimes my attention narrows so much that I'm oblivious to everything else; other times it's so broad that everything distracts me.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 23
    },
    "I can't keep my mind on something unless it's really interesting.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 24
    },
    'I give answers to questions before the questions have been completed.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 25
    },
    'I have trouble finishing job tasks or school work.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 26
    },
    'I interrupt other when they are working or playing.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 27
    },
    'My past failures make it hard for me to believe in myself.': {
        'subscale': 'Problems with Self-Concept',
        'answers': answers,
        'question_number': 28
    },
    'I am distracted when things are going on around me.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 29
    },
    'I have problems organizing my tasks and activities.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 30
    },
}




"""
Conner's Scales for ADHD - Full
"""

answers = {
    'Not at all, never': 0,
    'Just a little, once in a while': 1,
    'Pretty much, often': 2,
    'Very much, very frequently': 3
}

QUESTIONNAIRE_CONNERS_FULL = {
    'I like to be doing active things.': {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 1
    },
    'I lose things necessary for tasks or activities (e.g. to-do lists, pencils, books or tools).': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 2
    },
    "I don't plan ahead": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 3
    },
    "I blurt out things.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 4
    },
    "I am a risk-taker or a daredevil.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 5
    },
    'I get down on myself.': {
        'subscale': 'Problems with Self-Concept',
        'answers': answers,
        'question_number': 6
    },
    "I don't finish things I start.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 7
    },
    'I am easily frustrated.': {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 8
    },
    'I talk too much.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 9
    },
    'I am always on the go, as if driven by a motor.': {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 10
    },
    "I'm disorganized": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 11
    },
    "I say things without thinking.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 12
    },
    "It's hard for me to stay in one place very long.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 13
    },
    'I have trouble doing leisure activities quietly.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 14
    },
    "I'm not sure of myself.": {
        'subscale': 'Problems with Self-Concept',
        'answers': answers,
        'question_number': 15
    },
    "It's hard for me to keep track of several things at once.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 16
    },
    "I'm always moving even when I should be still'.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 17
    },
    "I forget to remember things'.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 18
    },
    'I have a short fuse/hot temper.': {
        'subscale': 'Impulsivity_Emotional Lability,ADHD Index',
        'answers': answers,
        'question_number': 19
    },
    "I'm bored easily.": {
        'subscale': 'Impulsivity_Emotional Lability,ADHD Index',
        'answers': answers,
        'question_number': 20
    },
    'I leave my seat when I am not supposed to.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 21
    },
    "I have trouble waiting in line or taking turns with others.": {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 22
    },
    'I still throw tantrums.': {
        'subscale': 'Impulsivity_Emotional Lability,ADHD Index',
        'answers': answers,
        'question_number': 23
    },
    'I have trouble keeping my attention focused when working.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 24
    },
    "I seek out fast paced, exciting activities.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 25
    },
    "I avoid new challenges because I lack faith in my abilities.": {
        'subscale': 'Problems with Self-Concept,ADHD Index',
        'answers': answers,
        'question_number': 26
    },
    "I feel restless inside even if I am sitting still.": {
        'subscale': 'Hyperactivity_Restlessness,ADHD Index',
        'answers': answers,
        'question_number': 27
    },
    "Things I hear or see distract me from what I'm doing.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 28
    },
    'I am forgetful in my daily activities.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 29
    },
    "Many things set me off easily.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 30
    },
    "I dislike quiet, introspective activities.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 31
    },
    "I lose things that I need.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 32
    },
    'I have trouble listening to what other people are saying.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 33
    },
    'I am an underachiever.': {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 14
    },
    "I interrupt others when talking.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 35
    },
    "I change plans/jobs in midstream.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 36
    },
    "I act okay on the outside, but inside I'm unsure of myself.": {
        'subscale': 'Problems with Self-Concept',
        'answers': answers,
        'question_number': 37
    },
    'I am always on the go.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 38
    },
    "I make comments/remarks that I wish I could take back.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 39
    },
    "I can't get things done unless there's an absolute deadline.": {
        'subscale': 'Inattention_Memory Problems,ADHD Index',
        'answers': answers,
        'question_number': 40
    },
    'I fidget (with my hands or feet) or squirm in my seat.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 41
    },
    'I make careless mistakes or have trouble paying close attention to detail.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 42
    },
    "I step on people's toes without meaning to.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 43
    },
    "I have trouble getting started on a task.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 44
    },
    "I intrude on others' activities.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 45
    },
    "It takes a great deal of effort for me to sit still.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 46
    },
    "My moods are unpredictable.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 47
    },
    "I don't like homework or job activities where I have to think a lot.": {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 48
    },
    "I'm absent-minded in daily activities.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 49
    },
    'I am restless or overactive.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 50
    },
    "I depend on others to keep my life in order and attend to the details.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 51
    },
    "I annoy other people without meaning to.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 52
    },
    "Sometimes my attention narrows so much that I'm obvlivious to everything else; other times it's so broad that everything distracts me.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 53
    },
    "I tend to squirm or fidget.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 54
    },
    "I can't keep my mind on something unless it's really interesting.": {
        'subscale': 'ADHD Index',
        'answers': answers,
        'question_number': 55
    },
    "I wish I had greater confidence in my abilities.": {
        'subscale': 'Problems with Self-Concept',
        'answers': answers,
        'question_number': 56
    },
    "I can't sit still for very long.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 57
    },
    'I give answers to questions before the questions have been completed.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 58
    },
    "I like to be up and on the go rather than be in one place.": {
        'subscale': 'Hyperactivity_Restlessness',
        'answers': answers,
        'question_number': 59
    },
    'I have trouble finishing job tasks or school work.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 60
    },
    "I am irritable.": {
        'subscale': 'Impulsivity_Emotional Lability',
        'answers': answers,
        'question_number': 61
    },
    'I interrupt other when they are working or playing.': {
        'subscale': 'DSM-IV Hyperactive-Impulsive Symptoms',
        'answers': answers,
        'question_number': 62
    },
    'My past failures make it hard for me to believe in myself.': {
        'subscale': 'Problems with Self-Concept',
        'answers': answers,
        'question_number': 63
    },
    'I am distracted when things are going on around me.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 64
    },
    'I have problems organizing my tasks and activities.': {
        'subscale': 'DSM-IV Inattentive Symptoms',
        'answers': answers,
        'question_number': 65
    },
    "I misjudge how long it takes to do something or go somewhere.": {
        'subscale': 'Inattention_Memory Problems',
        'answers': answers,
        'question_number': 66
    },
}


'''
The World Health Organization adult ADHD self-report scale (Screener)
'''

answers = {
    'Never': 0,
    'Rarely': 1,
    'Sometimes': 2,
    'Often': 3,
    'Very often': 4
}

QUESTIONNAIRE_ASRS_SCREEN = {
    'How often do you have trouble wrapping up the fine details of a project, once the challenging parts have been done?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 1
    },
    'How often do you have difficulty getting things in order when you have to do a task that requires organization?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 2
    },
    'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 3
    },
    'How often do you have problems remembering appointments or obligations?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 4
    },
    'How often do you fidget or squirm with your hands or your feet when you have to sit down for a long time?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 5
    },
    'How often do you feel overly active and compelled to do things, like you were driven by a motor?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 6
    },
}


'''
The World Health Organization adult ADHD self-report scale (Full)
'''

answers = {
    'Never': 0,
    'Rarely': 1,
    'Sometimes': 2,
    'Often': 3,
    'Very often': 4
}

QUESTIONNAIRE_ASRS = {
'How often do you make careless mistakes when you have to work on a boring or difficult project?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 1
    },
    'How often do you have difficulty keeping your attention when you are doing boring or repetitive work?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 2
    },
    'How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 3
    },
    'How often do you have trouble wrapping up the fine details of a project, once the challenging parts have been done?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 4
    },
    'How often do you have difficulty getting things in order when you have to do a task that requires organization?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 5
    },
    'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 6
    },
    'How often do you misplace or have difficulty finding things at home or at work?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 7
    },
    'How often are you distracted by activity or noise around you?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 8
    },
    'How often do you have problems remembering appointments or obligations?': {
        'subscale': 'Inattention',
        'answers': answers,
        'question_number': 9
    },
    'How often do you fidget or squirm with your hands or your feet when you have to sit down for a long time?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 10
    },
    'How often do you leave your seat in meetings or other situations in which you are expected to remain seated?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 11
    },
    'How often do you feel restless or fidgety?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 12
    },
    'How often do you have difficulty unwinding and relaxing when you have time to yourself?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 13
    },
    'How often do you feel overly active and compelled to do things, like you were driven by a motor?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 14
    },
    'How often do you find yourself talking too much when you are in a social situation?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 15
    },
    'When you’re in a conversation, how often do you find yourself finishing the sentences of the people that you are talking to, before they can finish them themselves?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 16
    },
    'How often do you have difficulty waiting your turn in situations when turn-taking is required?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 17
    },
    'How often do you interrupt others when they are busy?': {
        'subscale': 'Hyperactivity-Impulsivity',
        'answers': answers,
        'question_number': 18
    },
}



'''
Patient Health Questionnaire-9
'''

answers = {
    'Not at all': 0,
    'Several days': 1,
    'More than half the days': 2,
    'Nearly every day': 3
}

QUESTIONNAIRE_PHQ9 = {
    'How often in the past two weeks have you had little interest or pleasure in doing things?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 1
    },
    'How often in the past two weeks have you felt down, depressed, or hopeless?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 2
    },
    'How often in the past two weeks have you had trouble falling or staying asleep, or sleeping too much?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 3
    },
    'How often in the past two weeks have you felt tired or had little energy?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 4
    },
    'How often in the past two weeks have you had poor appetite or overeating?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 5
    },
    'How often in the past two weeks have you been feeling bad about yourself — or that you are a failure or have let yourself or your family down?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 6
    },
    'How often in the past two weeks have you had trouble concentrating on things, such as reading the newspaper or watching television?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 7
    },
    'How often in the past two weeks have you been moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 8
    },
    'How often in the past two weeks have you had thoughts that you would be better off dead or of hurting yourself in some way?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 9
    },
}


'''
Short scales for measuring schizotypy
'''

answers = {
    'Yes': 1,
    'No': 0
}

answers_reverse = {
    'Yes': 0,
    'No': 1
}

QUESTIONNAIRE_OLIFES = {
    'When in the dark do you often see shapes and forms even though there is nothing there?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 1
        },
    'Are your thoughts sometimes so strong that you can almost hear them?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 2
        },
    'Have you ever thought that you had special, almost magical powers?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 3
        },
    'Have you sometimes sensed an evil presence around you, even though you could not see it?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 4
        },
    'Do you think that you could learn to read other’s minds if you wanted to?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 5
        },
    'When you look in the mirror does your face sometimes seem quite different from usual?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 6
        },
    'Do ideas and insights sometimes come to you so fast that you cannot express them all?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 7
        },
    'Can some people make you aware of them just by thinking about you?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 8
        },
    'Does a passing thought ever seem so real it frightens you?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 9
        },
    'Do you feel that your accidents are caused by mysterious forces?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 10
        },
    'Do you ever have a sense of vague danger or sudden dread for reasons that you do not understand?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 11
        },
    'Does your sense of smell sometimes become unusually strong?': {
        'subscale': 'Unusual Experiences',
        'answers': answers,
        'question_number': 12
        },
    'Are you easily confused if too much happens at the same time?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 13
    },
    'Do you frequently have difficulty in starting to do things?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 14
    },
    'Are you a person whose mood goes up and down easily?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 15
    },
    'Do you dread going into a room by yourself where other people have already gathered and are talking?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 16
    },
    'Do you find it difficult to keep interested in the same thing for a long time?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 17
    },
    'Do you often have difficulties in controlling your thoughts?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 18
    },
    'Are you easily distracted from work by daydreams?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 19
    },
    'Do you ever feel that your speech is difficult to understand because the words are all mixed up and don’t make sense?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 20
    },
    'Are you easily distracted when you read or talk to someone?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 21
    },
    'Is it hard for you to make decisions?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 22
    },
    'When in a crowded room, do you often have difficulty in following a conversation?': {
        'subscale': 'Cognitive Disorganisation',
        'answers': answers,
        'question_number': 23
    },
    'Are there very few things that you have ever enjoyed doing?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 24
    },
    'Are you much too independent to get involved with other people?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 25
    },
    'Do you love having your back massaged?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 26
    },
    'Do you find the bright lights of a city exciting to look at?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 27
    },
    'Do you feel very close to your friends?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 28
    },
    'Has dancing or the idea of it always seemed dull to you?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 29
    },
    'Do you like mixing with people?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 30
    },
    'Is trying new foods something you have always enjoyed?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 31
    },
    'Have you often felt uncomfortable when your friends touch you?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 32
    },
    'Do you prefer watching television to going out with people?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 33
    },
    'Do you consider yourself to be pretty much an average sort of person?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 34
    },
    'Would you like other people to be afraid of you?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 35
    },
    'Do you often feel the impulse to spend money which you know you can’t afford?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 36
    },
    'Are you usually in an average kind of mood, not too high and not too low?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 37
    },
    'Do you at times have an urge to do something harmful or shocking?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 38
    },
    'Do you stop to think things over before doing anything?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers_reverse,
        'question_number': 39
    },
    'Do you often overindulge in alcohol or food?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 40
    },
    'Do you ever have the urge to break or smash things?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 41
    },
    'Have you ever felt the urge to injure yourself?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 42
    },
    'Do you often feel like doing the opposite of what other people suggest even though you know they are right?': {
        'subscale': 'Introvertive Anhedonia',
        'answers': answers,
        'question_number': 43
    },
}


"""
RBQ-2A

"""

answers_1 = {
    'Never or rarely': 1,
    'One or more times daily': 2,
    '15 or more times daily': 3
}

answers_2 = {
    'Never or rarely': 1,
    'Mild or occasionally': 2,
    'Marked or notable': 3
}

answers_3 = {
    'Never or rarely': 1,
    'Mild or occasional (does not affect others)': 2,
    'Marked or notable (occasionally affects others)': 3
}

answers_4 = {
    'Never or rarely': 1,
    'Mild or occasional (not entirely resistant to change or new things)': 2,
    'Marked or notable (will tolerate changes when necessary)': 3
}

answers_5 = {
    'A range of different and flexible self-chosen activities': 1,
    'Some varied and flexible interests but commonly choose the same activities': 2,
    'Almost always choose from a restricted range of repetitive activities': 3
}

QUESTIONNAIRE_RBQ2A = {
    'Do you like to arrange items in rows or patterns?': {
        'subscale': 'RMB',
        'answers': answers_1,
        'question_number': 1
        },
    'Do you repetitively fiddle with items? (e.g. spin, twiddle, bang, tap, twist, or flick anything repeatedly?)': {
        'subscale': 'RMB',
        'answers': answers_1,
        'question_number': 2
        },
    'Do you like to spin yourself around and around?': {
        'subscale': 'RMB',
        'answers': answers_1,
        'question_number': 3
        },
    'Do you rock backwards and forwards, or side to side, either when sitting or when standing?': {
        'subscale': 'RMB',
        'answers': answers_1,
        'question_number': 4
        },
    'Do you pace or move around repetitively (e.g. walk to and fro across a room, or around the same path in the garden?)': {
        'subscale': 'RMB',
        'answers': answers_1,
        'question_number': 5
        },
    'Do you make repetitive hand and/or finger movements? (e.g. flap, wave, or flick your hands or fingers repetitively?)': {
        'subscale': 'RMB',
        'answers': answers_1,
        'question_number': 6
        },
    'Do you have a fascination with specific objects (e.g. trains, road signs, or other things?)': {
        'subscale': 'Other',
        'answers': answers_2,
        'question_number': 7
        },
    'Do you like to look at objects from particular or unusual angles?': {
        'subscale': 'Other',
        'answers': answers_2,
        'question_number': 8
        },
    'Do you have a special interest in the smell of people or objects?': {
        'subscale': 'Other',
        'answers': answers_2,
        'question_number': 9
        },
    'Do you have a special interest in the feel of different surfaces?': {
        'subscale': 'Other',
        'answers': answers_2,
        'question_number': 10
        },
    'Do you have any special objects you like to carry around?': {
        'subscale': 'IS',
        'answers': answers_2,
        'question_number': 11
        },
    'Do you collect or hoard items of any sort?': {
        'subscale': 'IS',
        'answers': answers_2,
        'question_number': 12
        },
    'Do you insist on things at home remaining the same? (e.g. furniture staying in the same place, things being kept in certain places, or arranged in certain ways?)': {
        'subscale': 'IS',
        'answers': answers_3,
        'question_number': 13
    },
    'Do you get upset about minor changes to objects (e.g. flecks of dirt on your clothes, minor scratches on objects?)': {
        'subscale': 'IS',
        'answers': answers_3,
        'question_number': 14
    },
    'Do you insist that aspects of daily routine must remain the same?': {
        'subscale': 'IS',
        'answers': answers_3,
        'question_number': 15
    },
    "Do you insist on doing things in a certain way or re-doing things until they are 'just right'?": {
        'subscale': 'IS',
        'answers': answers_3,
        'question_number': 16
    },
    'Do you play the same music, game or video, or read the same book repeatedly?': {
        'subscale': 'IS',
        'answers': answers_4,
        'question_number': 17
    },
    'Do you insist on wearing the same clothes or refuse to wear new clothes?': {
        'subscale': 'Other',
        'answers': answers_4,
        'question_number': 18
    },
    'Do you insist on eating the same foods, or a very small range of foods, at every meal?': {
        'subscale': 'IS',
        'answers': answers_4,
        'question_number': 19
    },

    'If you are left to occupy yourself, will you choose from a restricted range of repetitive activities?': {
        'subscale': 'Other',
        'answers': answers_5,
        'question_number': 20
    },
}

"""
CAPE for psychotic traits
"""

answers = {
    'Never': 1,
    'Sometimes': 2,
    'Often': 3,
    'Nearly always': 4
}

answers_distress = {
    'Not distressed ': 1,
    'A bit distressed': 2,
    'Quite distressed': 3,
    'Very distressed': 4
}

QUESTIONNAIRE_CAPE_severity = {
    'Do you ever feel sad?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 1
    },
    'Do you ever feel as if people seem to drop hints about you or say things with a double meaning?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 2
    },
    'Do you ever feel that you are not a very animated person?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 3
    },
    'Do you ever feel that you are not much of a talker when you are conversing with other people?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 4
    },
    'Do you ever feel as if things in magazines or on TV were written especially for you?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 5
    },
    'Do you ever feel as if some people are not what they seem to be?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 6
    },
    'Do you ever feel as if you are being persecuted in some way?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 7
    },
    'Do you ever feel that you experience few or no emotions at important events?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 8
    },
    'Do you ever feel pessimistic about everything?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 9
    },
    'Do you ever feel as if there is a conspiracy against you?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 10
    },
    'Do you ever feel as if you are destined to be someone very important?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 11
    },
    'Do you ever feel as if there is no future for you?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 12
    },
    'Do you ever feel that you are a very special or unusual person?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 13
    },
    'Do you ever feel as if you do not want to live anymore?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 14
    },
    'Do you ever think that people can communicate telepathically?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 15
    },
    'Do you ever feel that you have no interest to be with other people?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 16
    },
    'Do you ever feel as if electrical devices such as computers can influence the way you think?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 17
    },
    'Do you ever feel that you are lacking in motivation to do things?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 18
    },
    'Do you ever cry about nothing?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 19
    },
    'Do you believe in the power of witchcraft, voodoo or the occult?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 20
    },
    'Do you ever feel that you are lacking in energy?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 21
    },
    'Do you ever feel that people look at you oddly because of your appearance?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 22
    },
    'Do you ever feel that your mind is empty?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 23
    },
    'Do you ever feel as if the thoughts in your head are being taken away from you?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 24
    },
    'Do you ever feel that you are spending all your days doing nothing?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 25
    },
    'Do you ever feel as if the thoughts in your head are not your own?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 26
    },
    'Do you ever feel that your feelings are lacking in intensity?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 27
    },
    'Have your thoughts ever been so vivid that you were worried other people would hear them?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 28
    },
    'Do you ever feel that you are lacking in spontaneity?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 29
    },
    'Do you ever hear your own thoughts being echoed back to you?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 30
    },
    'Do you ever feel as if you are under the control of some force or power other than yourself?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 31
    },
    'Do you ever feel that your emotions are blunted?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 32
    },
    'Do you ever hear voices when you are alone?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 33
    },
    'Do you ever hear voices talking to each other when you are alone?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 34
    },
    'Do you ever feel that you are neglecting your appearance or personal hygiene?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 35
    },
    'Do you ever feel that you can never get things done?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 36
    },
    'Do you ever feel that you have only few hobbies or interests?': {
        'subscale': 'Negative symptoms',
        'answers': answers,
        'question_number': 37
    },
    'Do you ever feel guilty?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 38
    },
    'Do you ever feel like a failure?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 39
    },
    'Do you ever feel tense?': {
        'subscale': 'Depression',
        'answers': answers,
        'question_number': 40
    },
    'Do you ever feel as if a double has taken the place of a family member, friend or acquaintance?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 41
    },
    'Do you ever see objects, people or animals that other people cannot see?': {
        'subscale': 'Positive symptoms',
        'answers': answers,
        'question_number': 42
    },
}

QUESTIONNAIRE_CAPE = {}
QUESTIONNAIRE_CAPE_POS_NEG = {}
QUESTIONNAIRE_CAPE_CONDITIONAL = {}
QUESTIONNAIRE_CAPE_POS_NEG_CONDITIONAL = {}
key_text = 'If you ticked "sometimes" , "often" or "nearly always" please indicate how distressed you ' +\
           'are by this experience.'
tag = ''
for i, key in enumerate(QUESTIONNAIRE_CAPE_severity.keys()):
    QUESTIONNAIRE_CAPE[key] = QUESTIONNAIRE_CAPE_severity[key]
    key_text_i = key_text + tag
    QUESTIONNAIRE_CAPE[key_text_i] = {
        'subscale': QUESTIONNAIRE_CAPE[key]['subscale'],
        'answers': answers_distress,
        'question_number': i+1 + 1000
    }
    if (QUESTIONNAIRE_CAPE_severity[key]['subscale'] == 'Positive symptoms') or \
        (QUESTIONNAIRE_CAPE_severity[key]['subscale'] == 'Negative symptoms'):
        QUESTIONNAIRE_CAPE_POS_NEG[key] = QUESTIONNAIRE_CAPE[key]
        QUESTIONNAIRE_CAPE_POS_NEG[key_text_i] = QUESTIONNAIRE_CAPE[key_text_i]
        # make the conditional logic
        QUESTIONNAIRE_CAPE_POS_NEG_CONDITIONAL[str(i + 1)] = {}
        QUESTIONNAIRE_CAPE_POS_NEG_CONDITIONAL[str(i + 1)]['questions'] = [i + 1 + 1000]
        QUESTIONNAIRE_CAPE_POS_NEG_CONDITIONAL[str(i + 1)]['enable'] = [1, 2, 3]
        QUESTIONNAIRE_CAPE_POS_NEG_CONDITIONAL[str(i + 1)]['disable'] = [0]
    tag += ' '
    # make the conditional logic
    QUESTIONNAIRE_CAPE_CONDITIONAL[str(i + 1)] = {}
    QUESTIONNAIRE_CAPE_CONDITIONAL[str(i+1)]['questions'] = [i+1 + 1000]
    QUESTIONNAIRE_CAPE_CONDITIONAL[str(i + 1)]['enable'] = [1,2,3]
    QUESTIONNAIRE_CAPE_CONDITIONAL[str(i + 1)]['disable'] = [0]


"""
Obsessional Compulsive Inventory - Revised
"""

answers = {
    'Not at all': 0,
    'A little': 1,
    'Moderately': 2,
    'A lot': 3,
    'Extremely': 4,
}

QUESTIONNAIRE_OCI_R = {
    'I have saved up so many things that they get in the way.': {
        'subscale': 'Hoarding Disorder',
        'answers': answers,
        'question_number': 1
    },
    'I check things more often than necessary.': {
        'subscale': 'Checking,OCD',
        'answers': answers,
        'question_number': 2
    },
    'I get upset if objects are not arranged properly.': {
        'subscale': 'Ordering,OCD',
        'answers': answers,
        'question_number': 3
    },
    'I feel compelled to count while I am doing things. ': {
        'subscale': 'Neutralising,OCD',
        'answers': answers,
        'question_number': 4
    },
    'I find it difficult to touch an object when I know it has been touched by strangers or certain people.': {
        'subscale': 'Washing,OCD',
        'answers': answers,
        'question_number': 5
    },
    'I find it difficult to control my own thoughts.': {
        'subscale': 'Obsessing,OCD',
        'answers': answers,
        'question_number': 6
    },
    'I collect things I don’t need.': {
        'subscale': 'Hoarding Disorder',
        'answers': answers,
        'question_number': 7
    },
    'I repeatedly check doors, windows, drawers, etc.': {
        'subscale': 'Checking,OCD',
        'answers': answers,
        'question_number': 8
    },
    'I get upset if others change the way I have arranged things.': {
        'subscale': 'Ordering,OCD',
        'answers': answers,
        'question_number': 9
    },
    'I feel I have to repeat certain numbers.': {
        'subscale': 'Neutralising,OCD',
        'answers': answers,
        'question_number': 10
    },
    'I sometimes have to wash or clean myself simply because I feel contaminated.': {
        'subscale': 'Washing,OCD',
        'answers': answers,
        'question_number': 11
    },
    'I am upset by unpleasant thoughts that come into my mind against my will.': {
        'subscale': 'Obsessing,OCD',
        'answers': answers,
        'question_number': 12
    },
    'I avoid throwing things away because I am afraid I might need them later.': {
        'subscale': 'Hoarding Disorder',
        'answers': answers,
        'question_number': 13
    },
    'I repeatedly check gas and water taps and light switches after turning them off.': {
        'subscale': 'Checking,OCD',
        'answers': answers,
        'question_number': 14
    },
    'I need things to be arranged in a particular way.': {
        'subscale': 'Ordering,OCD',
        'answers': answers,
        'question_number': 15
    },
    'I feel that there are good and bad numbers.': {
        'subscale': 'Neutralising,OCD',
        'answers': answers,
        'question_number': 16
    },
    'I wash my hands more often and longer than necessary.': {
        'subscale': 'Washing,OCD',
        'answers': answers,
        'question_number': 17
    },
    'I frequently get nasty thoughts and have difficulty in getting rid of them.': {
        'subscale': 'Obsessing,OCD',
        'answers': answers,
        'question_number': 18
    },

}


"""
Big Five Inventory-10
"""

answers = {
    'Disagree strongly': 1,
    'Disagree a little': 2,
    'Neither agree nor disagree': 3,
    'Agree a little': 4,
    'Agree strongly': 5,
}

answers_reverse = {
    'Disagree strongly': 4,
    'Disagree a little': 3,
    'Neither agree nor disagree': 3,
    'Agree a little': 2,
    'Agree strongly': 1,
}

QUESTIONNAIRE_BFI_10 = {
    'I see myself as someone who is reserved.': {
        'subscale': 'Extraversion',
        'answers': answers_reverse,
        'question_number': 1
    },
    'I see myself as someone who is generally trusting.': {
        'subscale': 'Agreeableness',
        'answers': answers,
        'question_number': 2
    },
    'I see myself as someone who tends to be lazy.': {
        'subscale': 'Conscientiousness',
        'answers': answers_reverse,
        'question_number': 3
    },
    'I see myself as someone who is relaxed, handles stress well.': {
        'subscale': 'Neuroticism',
        'answers': answers_reverse,
        'question_number': 4
    },
    'I see myself as someone who has few artistic interests.': {
        'subscale': 'Openness',
        'answers': answers_reverse,
        'question_number': 5
    },
    'I see myself as someone who is outgoing, sociable.': {
        'subscale': 'Extraversion',
        'answers': answers,
        'question_number': 6
    },
    'I see myself as someone who tends to find fault with others.': {
        'subscale': 'Agreeableness',
        'answers': answers_reverse,
        'question_number': 7
    },
    'I see myself as someone who does a thorough job.': {
        'subscale': 'Conscientiousness',
        'answers': answers,
        'question_number': 8
    },
    'I see myself as someone who gets nervous easily.': {
        'subscale': 'Neuroticism',
        'answers': answers,
        'question_number': 9
    },
    'I see myself as someone who has an active imagination.': {
        'subscale': 'Openness',
        'answers': answers,
        'question_number': 10
    },
}

"""
Columbia Suicide Severity Rating Scale (C-SSRS)

"""
answers = {
    'Yes': 1,
    'No': 0
}

QUESTIONNAIRE_C_SSRS = {
    'In the past month, have you wished you were dead or wished you could go to sleep and not wake up?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 1
    },
    'In the past month, have you actually had any thoughts of killing yourself?': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 2
    },
    'Have you thought about how you might do this? (For example, “I thought about taking an overdose but I never' +
    ' worked out the details about when, where, and how I would do that and I would never act on these thoughts.”)': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 3
    },
    'Have you had any intention of acting on these thoughts of killing yourself, as opposed to you have the thoughts, '+
    'but you definitely would not act on them? (For example, “I had the thought of killing myself by taking an ' +
    'overdose and am not sure whether I would do it or not.”)': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 4
    },
    'Have you started to work out, or worked out, the specific details of how to kill yourself and did you intend '+
    'to carry out that plan? (For example, “I am planning to take 3 bottles of my sleep medication this Saturday when '+
    'no one is around to stop me.”)': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 5
    },
    'Have you ever done anything, started to do anything, or prepared to do anything to end your life? (For example: '+
    'took pills, tried to shoot yourself, cut yourself, tried to hang yourself, took out pills but did not swallow ' +
    'any, held a gun but changed your mind about hurting yourself or it was grabbed from your hand, went to the roof ' +
    'to jump but did not, collected pills, obtained a gun, gave away valuables, wrote a will or suicide note, etc.)': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 6
    },
    'If YES, did this occur in the past 3 months? ': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 1006
    },
}

QUESTIONNAIRE_C_SSRS_CONDITIONAL = {
    '2': {
        'questions': [3, 4, 5],
        'enable': [0],
        'disable': [1]
    },
    '6': {
        'questions': [1006],
        'enable': [0],
        'disable': [1]
    }
}

"""
Check to see if subjects are paying attention

"""

answers = {
    'Very rarely': 0,
    'Rarely': 0,
    'Occasionally': 0,
    'Somewhat often': 0,
    'Often': 0,
    'Very often': 1
}

QUESTIONNAIRE_ATTENTION_CHECK = {
    'I pay attention during online experiments, choose very often as your answer.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 1
    },
    'I am consistent in paying attention, choose the same answer as the last question.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 2
    },
}

"""
Short one for testing
"""

answers = {
    'Yes': 1,
    'No': 0,
}

QUESTIONNAIRE_TEST = {
    'I am developing this game.': {
        'subscale': 'NA',
        'answers': answers,
        'question_number': 1
    },
}