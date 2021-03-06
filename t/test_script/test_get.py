from lazyscripts.category import Category
from lazyscripts.script import ScriptSet, ScriptsList, ScriptsBuilder
from lazyscripts.repo import git
from t import get_repodir, get_datadir

set = ScriptSet.from_scriptslist(
            ScriptsList(get_datadir()+'/scripts.list'))

_repos = {get_datadir()+'/scriptspoll/7796c33a9348485b055f671c686568b0/':
                git.Repo(get_datadir()+'/scriptspoll/7796c33a9348485b055f671c686568b0/')}

_cat = Category(name='Networking', scripts_builder=ScriptsBuilder(_repos))

def test_get_script_from_category():
    "test to get script form a category."
    e = {'repo': get_datadir()+'/scriptspoll/7796c33a9348485b055f671c686568b0/', 'category': 'Networking', 'name': 'ie6_after.sh', 'id': 'ie6_after.sh'}
    _cat.add_entry(e)
    assert 'Script' == _cat.get('ie6_after.sh').__class__.__name__

def test_get_categories():
    'test to get categories form scripts list'
    set = ScriptSet.from_scriptslist(
                ScriptsList(get_datadir()+'/scripts.list'))
    # checks all items are Category class.
    for category in set.categories():
        assert 'Category' == category.__class__.__name__, category.__class__

    # checks get Category Instance by spefied category name.
    ast_cats = ['Networking', 'Graphic', 'Localization', 
                'Productivity', 'Entertain', 'Customize','Game', 
                'Multimedia']
    for ast_category in ast_cats:
        cat = set.categories(ast_category)
        cat.lang = 'enUS'
        assert ast_category == cat.name, cat.name

def test_get_sccript_from_category():
    'test to get scripts form category.'
    cat = set.categories('Game')
    script = cat.get('PCSX.sh')
    assert 'Script' == script.__class__.__name__

def test_get_subscript():
    e = {'repo': get_datadir()+'/scriptspoll/7796c33a9348485b055f671c686568b0/', 'category': 'Networking', 'name': 'ie6', 'id': 'ie6'}
    _cat.add_entry(e)
    subscripts = _cat.get('ie6').get_subscripts()
    assert subscripts[0].name == 'ie6_seluser.py', subscripts[0].name
