import json
from collections import defaultdict
aliases = defaultdict(lambda: {})

def main():
	# Presidential
	aliases['1960']['John F. Kennedy'] = [u'Mr. KENNEDY', u'SENATOR KENNEDY', u'MR. KENNEDY', u'John F. Kennedy']
	aliases['1960']['Richard Nixon'] = [u'MR. NIXON', u'Mr. NIXON', u'Richard Nixon']
	# Presidential
	aliases['1976']['Gerald Ford'] = [u'THE PRESIDENT.', u'Gerald Ford']
	aliases['1976']['Jimmy Carter'] = [u'MR. CATER.', u'MR. CARTER.', u'Jimmy Carter']
	# Presidential
	aliases['1980']['Ronald Reagan'] = [u'REAGAN', u'GOV. RONALD REAGAN', u'GOVERNOR REAGAN.']
	aliases['1980']['John Anderson'] = [u'ANDERSON', u'REP. JOHN B. ANDERSON']
	aliases['1980']['Jimmy Carter'] = [u'THE PRESIDENT.']
	# Presidential
	aliases['1984']['Ronald Reagan'] = [u'The President.',u'Mr. President.']
	aliases['1984']['Walter F. Mondale'] = [u'Mr. Mondale.']
	# Presidential
	aliases['1988']['George H. W. Bush'] = [u'BUSH']
	aliases['1988']['Michael Dukakis'] = [u'DUKAKIS']
	# Presidential
	aliases['1992']['Bill Clinton'] = [u'Governor Clinton.']
	aliases['1992']['George H. W. Bush'] = [u'President Bush.', u'Mr. President.']
	aliases['1992']['Ross Perot'] = [u'Mr. Perot.']
	# Presidential
	aliases['1996']['Bill Clinton'] = [u'The President.', u'Mr. President.']
	aliases['1996']['Bob Dole'] = [u'Senator Dole.']
	# Democratic
	aliases['2000']['Al Gore'] = [u'Gore']
	aliases['2000']['Bill Bradley'] = [u'Bradley', u'Senator Bradley.']
	# Presidential
	aliases['2000']['George W. Bush'] = [u'BUSH']
	aliases['2000']['Al Gore'] = [u'GORE']
	# Republican
	aliases['2000']['George W. Bush'] = [u'Bush', u'BUSH', u'Governor Bush.']
	aliases['2000']['Gary Bauer'] = [u'Mr. Bauer.', u'Bauer', u'GARY BAUER', u'BAUER']
	aliases['2000']['Steve Forbes'] = [u'Forbes', u'Mr. Forbes.', u'STEVE FORBES', u'FORBES']
	aliases['2000']['Orrin Hatch'] = [u'HATCH', u'Hatch', u'Senator Hatch.', u'SEN. ORRIN HATCH', u'Mr. Hatch.']
	aliases['2000']['Alan Keyes'] = [u'Mr. Keyes.', u'KEYES', u'ALAN KEYES', u'Keyes']
	aliases['2000']['John McCain'] = [u'MCCAIN', u'SENATOR JOHN McCAIN', u'McCain', u'McCAIN', u'SEN. JOHN McCAIN']
	# Democratic
	aliases['2004']['Wesley Clark'] = [ u'GEN. WESELEY CLARK, (D) PRESIDENTIAL CANDIDATE', u'CLARK', u'Wesley Clark']
	aliases['2004']['John Edwards'] = [ u'SEN. JOHN EDWARDS, (D-NC) PRESIDENTIAL CANDIDATE', u'EDWARDS', u'John Edwards']
	aliases['2004']['Joe Lieberman'] = [u'SEN. JOE LIEBERMAN, (D-CT) PRESIDENTIAL CANDIDATE', u'LIEBERMAN', u'Joe Lieberman']
	aliases['2004']['Dennis Kucinich'] = [u'REP. DENNIS KUCINICH, (D-OH) PRESIDENTIAL CANDIDATE', u'KUCINICH', u'Dennis Kucinich']
	aliases['2004']['Al Sharpton'] = [u'REV. AL SHARPTON, (D) PRESIDENTIAL CANDIDATE', u'SHARPTON', u'Al Sharpton']
	aliases['2004']['Howard Dean'] = [u'HOWARD DEAN, (D-VT) PRESIDENTIAL CANDIDATE', u'DEAN', u'Howard Dean']
	# Presidential
	aliases['2004']['John Kerry'] = [ u'SEN. JOHN KERRY, (D-MA) PRESIDENTIAL CANDIDATE',  u'KERRY', u'Senator John F. Kerry.', u'Senator Kerry.', u'John Kerry']
	aliases['2004']['George W. Bush'] = [u'President Bush.', u'George W. Bush']
	# Republican
	aliases['2008']['Sam Brownback'] = [u'Brownback', u'BROWNBACK', u'Senator Brownback.', u'Senator Brownback', u'SEN. BROWNBACK', u'Senator Sam Brownback (R-Kan.)', u'Sam Brownback']
	aliases['2008']['Rudolph Giuliani'] = [u'Giuliani', u'GIULAINI', u'MR. GIULIANI', u'GIULIANI', u'Former New York City Mayor Rudolph Giuliani', u'MAYOR GIULIANI', u'Rudolph Giuliani']
	aliases['2008']['Mike Huckabee'] = [u'GOV. HUCKABEE', u'Former Arkansas Governor Mike Huckabee', u'Huckabee', u'HUCKABEE', u'MR. HUCKABEE', 'Mike Huckabee']
	aliases['2008']['Duncan Hunter'] = [u'Representative Duncan Hunter (R-Calif.)', u'REP. HUNTER', u'HUNTER', u'Hunter', u'Duncan Hunter']
	aliases['2008']['Ron Paul'] = [u'REP. PAUL', u'Representative Ron Paul (R-Texas)',  u'MR. PAUL', u'PAUL', u'Ron Paul']
	aliases['2008']['Mitt Romney'] = [u'Former Massachusetts Governor Mitt Romney', u'GOV. ROMNEY', u'ROMNEY', u'MR. ROMNEY', u'Romney', u'Mitt Romney']
	aliases['2008']['Tom Tancredo'] = [u'Representative Tom Tancredo (R-Col.)', u'Tancredo', u'REP. TANCREDO', u'TANCREDO', u'Tom Tancredo']
	aliases['2008']['Fred Thompson'] = [u'SEN THOMPSON', u'Fred Thompson']
	aliases['2008']['Tommy Thompson'] = [u'Former Wisconsin Governor Tommy Thompson', u'GOV. THOMPSON', u'Tommy Thompson']
	aliases['2008']['James Gilmore'] = [u'Former Virginia Governor James Gilmore (R-Va.)', u'GOV. GILMORE', u'James Gilmore']
	aliases['2008']['Alan Keyes'] = [u'AMB. KEYES', u'KEYES', u'Alan Keyes']
	# Democratic
	aliases['2008']['Joe Biden'] = [u'Biden', u'SEN. JOSEPH R. BIDEN JR., D-DEL.', u'SEN. BIDEN', u'BIDEN', u'Senator Biden.', u'Sen. Joseph R. Biden Jr.', u'Joe Biden']
	aliases['2008']['Hillary Clinton'] = [u'CLINTON', u'SEN. HILLARY RODHAM CLINTON, D-N.Y.', u'SENATOR CLINTON', u'Clinton', u'SEN. CLINTON', u'Sen. Hillary Rodham Clinton', u'Senator Clinton.', u'Hillary Clinton']
	aliases['2008']['Christopher Dodd'] = [u'Senator Dodd.', u'SEN. CHRISTOPHER J. DODD, D-CONN.', u'Dodd', u'SEN. DODD', u'Sen. Christopher J. Dodd', u'MR. DODD', u'Christopher Dodd']
	aliases['2008']['John Edwards'] = [u'EDWARDS', u'FORMER SEN. JOHN EDWARDS, D-N.C.', u'Senator Edwards.', u'MR. EDWARDS', u'SEN. EDWARDS', u'Edwards', u'Former Sen. John Edwards', u'John Edwards']
	aliases['2008']['Mike Gravel'] = [u'Former Sen. Mike Gravel', u'GRAVEL', u'MR. GRAVEL', u'Mike Gravel']
	aliases['2008']['Dennis Kucinich'] = [u'REP. KUCINICH', u'Senator Kucinich.', u'Kucinich', u'KUCINICH', u'Rep. Dennis J. Kucinich', u'Dennis Kucinich']
	aliases['2008']['Bill Richardson'] = [u'GOV. BILL RICHARDSON, D-N.M.', u'Richardson', u'RICHARDSON', u'GOV. RICHARDSON', u'Bill Richardson']
	# Presidential
	aliases['2008']['Barack Obama'] = [u'Senator Obama.', u'OBAMA', u'SEN. BARACK OBAMA, D-ILL.', u'Obama', u'SEN. OBAMA', u'SENATOR OBAMA', u'Barack Obama']
	aliases['2008']['John McCain'] = [u'SEN. MCCAIN', u'MCCAIN', u'McCain', 'John McCain']

	aliases['2012']['Barack Obama'] = [u'Barack Obama']
	aliases['2012']['Mitt Romney'] = [u'Mitt Romney']
	aliases['2012']['Michele Bachmann'] = [u'Michele Bachmann']
	aliases['2012']['Herman Cain'] = [u'Herman Cain']
	aliases['2012']['Newt Gingrich'] = [u'Newt Gingrich']
	aliases['2012']['Ron Paul'] = [u'Ron Paul']
	aliases['2012']['Tim Pawlenty'] = [u'Tim Pawlenty']
	aliases['2012']['Rick Santorum'] = [u'Rick Santorum']
	aliases['2012']['Jon Huntsman'] = [u'Jon Huntsman']
	aliases['2012']['Rick Perry'] = [u'Rick Perry']
	aliases['2012']['Gary Johnson'] = [u'Rick Johnson']
	aliases['2012']['Fred Karger'] = [u'Fred Karger']
	aliases['2012']['Buddy Roemer'] = [u'Buddy Roemer']
	aliases['2016']['Donald Trump'] = [u'Donald Trump']
	aliases['2016']['Ted Cruz'] = [u'Ted Cruz']
	aliases['2016']['Marco Rubio'] = [u'Marco Rubio']
	aliases['2016']['John Kasich'] = [u'John Kasich']
	aliases['2016']['Ben Carson'] = [u'Ben Carson']
	aliases['2016']['Jeb Bush'] = [u'Jeb Bush']
	aliases['2016']['Jim Gilmore'] = [u'Jim Gilmore']
	aliases['2016']['Chris Christie'] = [u'Chris Christie']
	aliases['2016']['Carly Fiorina'] = [u'Carly Fiorina']
	aliases['2016']['Rick Santorum'] = [u'Rick Santorum']
	aliases['2016']['Rand Paul'] = [u'Rand Paul']
	aliases['2016']['Mike Huckabee'] = [u'Mike Huckabee']
	aliases['2016']['Hillary Clinton'] = [u'Hillary Clinton']
	aliases['2016']['Bernie Sanders'] = [u'Bernie Sanders']
	aliases['2016']['Martin O\'Malley'] = [u'Martin O\'Malley']
	aliases['2016']['Vermin Supreme'] = [u'Vermin Supreme']
	new_file = open('aliases.json', "w")
	new_file.write(json.dumps(aliases))
	new_file.close()

if __name__ == '__main__':
	main()



