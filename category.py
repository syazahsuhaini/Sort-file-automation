from data_path import *

categories = {
    'Pictures' : {
        'Extensions' : ['.png', '.jpg', '.jpeg'],
        'Path' : pictures_dir
    },
    'Spreadsheets' : {
        'Extensions' : ['.csv'],
        'Path' : spreadsheets_dir
    },
    'Executables' : {
        'Extensions' : ['.exe'],
        'Path' : programs_dir
    },
    'Folders' : {
        'Extensions' : ['.zip'],
        'Path' : folders_dir
    },
    'Documents' : {
        'Extensions' : ['.pdf','.doc','.docx'],
        'Path' : documents_dir
    }
}