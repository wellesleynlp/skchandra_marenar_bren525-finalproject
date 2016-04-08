import json
from collections import defaultdict

def main():
	labels = {}
	labels['Al Gore democratic 2000'] = 1
	labels['Wesley Clark democratic 2004'] = 0
	labels['George W. Bush presidential 2004'] = 1
	labels['Rick Perry republican 2012'] = 0
	labels['Richard Nixon presidential 1960'] = 0
	labels['Newt Gingrich republican 2012'] = 0
	labels['John Edwards democratic 2004'] = 0
	labels['Dennis Kucinich democratic 2004'] = 0
	labels['Bob Dole presidential 1996'] = 0
	labels['John Anderson presidential 1980'] = 0
	labels['Tim Pawlenty republican 2012'] = 0
	labels['Jon Huntsman republican 2012'] = 0
	labels['Jimmy Carter presidential 1980'] = 0
	labels['Al Sharpton democratic 2004'] = 0
	labels['Rick Santorum republican 2012'] = 0
	labels['Herman Cain republican 2012'] = 0
	labels['Ronald Reagan presidential 1980'] = 1
	labels['Howard Dean democratic 2004'] = 0
	labels['Mitt Romney republican 2012'] = 1
	labels['Michael Dukakis presidential 1988'] = 0
	labels['John Kerry democratic 2004'] = 1
	labels['John Kerry presidential 2004'] = 0
	labels['Mitt Romney presidential 2012'] = 0
	labels['Buddy Roemer republican 2012'] = 0
	labels['George H. W. Bush presidential 1988'] = 1
	labels['Joe Lieberman democratic 2004'] = 0
	labels['Bill Clinton presidential 1996'] = 1
	labels['Barack Obama presidential 2012'] = 1
	labels['Michele Bachmann republican 2012'] = 0
	labels['Fred Karger republican 2012'] = 0
	labels['Ron Paul republican 2012'] = 0
	labels['John F. Kennedy presidential 1960'] = 1
	labels['John McCain presidential 2008'] = 0
	labels['Ben Carson republican 2016'] = 0
	labels['Jimmy Carter presidential 1976'] = 1
	labels['Marco Rubio republican 2016'] = 0
	labels['Jeb Bush republican 2016'] = 0
	labels['George W. Bush presidential 2000'] = 1
	labels['George H. W. Bush presidential 1992'] = 0
	labels['Tommy Thompson republican 2008'] = 0
	labels['John Edwards democratic 2008'] = 0
	labels['Dennis Kucinich democratic 2008'] = 0
	labels['Fred Thompson republican 2008'] = 0
	labels['Ron Paul republican 2008'] = 0
	labels['Al Gore presidential 2000'] = 0
	labels['Bernie Sanders democratic 2016'] = 0
	labels['Mike Huckabee republican 2008'] = 0
	labels['Alan Keyes republican 2008'] = 0
	labels['Bill Bradley democratic 2000'] = 0
	labels['Ross Perot presidential 1992'] = 0
	labels['Steve Forbes republican 2000'] = 0
	labels['John McCain republican 2008'] = 1
	labels['Ronald Reagan presidential 1984'] = 1
	labels['Bill Richardson democratic 2008'] = 0
	labels['Barack Obama democratic 2008'] = 1
	labels['Jim Gilmore republican 2016'] = 0
	labels['Vermin Supreme democratic 2016'] = 0
	labels['Rick Santorum republican 2016'] = 0
	labels['Gerald Ford presidential 1976'] = 0
	labels['Alan Keyes republican 2000'] = 0
	labels['Mitt Romney republican 2008'] = 0
	labels["Martin O'Malley democratic 2016"] = 0
	labels['Joe Biden democratic 2008'] = 0
	labels['Walter F. Mondale presidential 1984'] = 0
	labels['Rudolph Giuliani republican 2008'] = 0
	labels['Barack Obama presidential 2008'] = 1
	labels['Gary Bauer republican 2000'] = 0
	labels['George W. Bush republican 2000'] = 1
	labels['Duncan Hunter republican 2008'] = 0
	labels['Carly Fiorina republican 2016'] = 0
	labels['Bill Clinton presidential 1992'] = 1
	labels['John McCain republican 2000'] = 0
	labels['Donald Trump republican 2016'] = 0
	labels['Hillary Clinton democratic 2016'] = 0
	labels['Hillary Clinton democratic 2008'] = 0
	labels['Tom Tancredo republican 2008'] = 0
	labels['James Gilmore republican 2008'] = 0
	labels['Orrin Hatch republican 2000'] = 0
	labels['Christopher Dodd democratic 2008'] = 0
	labels['Mike Huckabee republican 2016'] = 0
	labels['Mike Gravel democratic 2008'] = 0
	labels['Ted Cruz republican 2016'] = 0
	labels['Sam Brownback republican 2008'] = 0
	labels['Chris Christie republican 2016'] = 0
	labels['Rand Paul republican 2016'] = 0
	labels['John Kasich republican 2016'] = 0
	new_file = open('win_loss_labels.json', "w")
	new_file.write(json.dumps(labels))
	new_file.close()

if __name__ == '__main__':
	main()