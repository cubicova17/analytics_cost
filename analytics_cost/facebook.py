#import urllib2
import requests
#req = urllib2.Request()
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip,deflate,sdch',
'Accept-Language':'en-US,en;q=0.8',
'Connection':'keep-alive',
'Cookie':'datr=ibhrUGhETDuh4UCGNBVa1UQB; lu=TgKp_HO092aNTH0ly-vaWoiQ; locale=en_US; c_user=1061404108; csm=2; fr=0CH8jDBkLmRIDNXbP.AWWcaQsA8YtmHL3rD8jAJIl4mzY.BQo8MU.Sd.AWWf3CqC; xs=1%3A_VURoszDaHTtIA%3A2%3A1354725061; pk=AcO8f7nn2cElNM8l; s=Aa68FD6IGDwcRtqE.BQ4gG-; p=114; presence=EM356989308EuserFA21061404108A2EstateFDsb2F1356679477229Et2F_5b_5dElm2FnullEuct2F1356986274BEtrFA2loadA2EtwF3379034537EatF1356989305208G356989308130CEchFDp_5f1061404108F2CC; wd=960x231; act=1356989515555%2F4%3A0; _e_05ZF_1=%5B%2205ZF%22%2C1356989515556%2C%22act%22%2C1356989515555%2C4%2C%22https%3A%2F%2Fwww.facebook.com%2Fads%2Fmanage%2Fview_report.php%3Fact%3D351379343%22%2C%22form%22%2C%22submit%22%2C%22-%22%2C%22r%22%2C%22%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C0%2C0%2C0%2C0%2C16%5D',
'Host':'www.facebook.com',
'Referer':'https://www.facebook.com/ads/manage/reports.php?act=351379343',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.101 Safari/537.11'
}
r = requests.get('https://www.facebook.com/ads/manage/view_report.php?act=351379343&report_type=perf&summarize_by=campaign&filter=nofilter&agg_time=daily&day_start_text_fieldIntlDisplay=11%2F1%2F2012&day_start_text_field=11%2F1%2F2012&day_end_text_fieldIntlDisplay=1%2F1%2F2013&day_end_text_field=1%2F1%2F2013&week_start_text_fieldIntlDisplay=12%2F9%2F2012&week_start_text_field=12%2F9%2F2012&week_end_text_fieldIntlDisplay=12%2F28%2F2012&week_end_text_field=12%2F28%2F2012&month_start_month=10&month_start_year=2012&month_end_month=12&month_end_year=2012&format=tsv', headers=headers)
print len(r.content)
with open("report.csv", "wb") as code:
    code.write(r.content)
