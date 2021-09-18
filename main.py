from meme import memes

nonRecurrent = {

}

recurrent = {
    'daily' : {
        'name': 'someDailyMeme',
        'file': '',        
        'hour': '',
    },
    'weekly' : {
        'Monday': [
            {
                'name': 'FelizJueves',
                'file': './recurrent/2_weekly/4_thrusday/feliz-jueves-asuka-4.jpg',
                'hour': '15:42'
            },
            {
                'name': 'FelizJueves',
                'file': './recurrent/2_weekly/4_thrusday/asuka-feliz-jueves-1.gif',
                'hour': '15:43'
            },
            {
                'name': 'FelizJueves',
                'file': './recurrent/2_weekly/4_thrusday/feliz-jueves-asuka-2.gif',
                'hour': '15:44'
            },
            {
                'name': 'FelizJueves',
                'file': './recurrent/2_weekly/4_thrusday/feliz-jueves-asuka-3.gif',
                'hour': '15:45'
            },
        ],
        'Tuesday': ['asuka', 'hadock'],
        'Wednesday': [
            {
                'name': 'HadockWeek',
                'file': '',
                'hour': ''
            },
        ],
        'Thursday': ['asuka', 'hadock'],
        'Friday': ['asuka', 'hadock'],
        'Saturday': ['asuka', 'hadock'],
        'Sunday': ['asuka', 'hadock']
    },   
    'monthly' : {
        'name': 'someMonthlyMeme',
        'file': '',        
        'day': '',
        'hour': '',
    }, 
    'yearly' : {
        'janaury': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'febreaury': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'march': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'april': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'may': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'june': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'july': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'august': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'september': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'october': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'november': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],
        'december': [
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
            {
                'name': '',
                'file': '',
                'date': '',
                'hour': '',
            },
        ],   
    }
}

def job():
    print("Time for post meme!")    

    
if __name__  == '__main__':
    memes(recurrent)
