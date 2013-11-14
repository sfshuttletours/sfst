RESELLER_HTML = """


<script language="javascript" type="text/javascript" src="/static/js/jquery.js"></script>
<style type="text/css">
      <!--
      @import url("/static/style_sheet.css");
      a.mytd{
            font-family: Geneva, Arial, Helvetica, sans-serif;
            font-weight:bold;
            font-size: 9pt; 
            padding:20px auto;
            }
      a.mytd2{
            font-family: Geneva, Arial, Helvetica, sans-serif;
            font-color:red;
            font-weight:bold;
            font-size: 9pt; 
            padding:20px auto;
            }
      h2.sites {
            font-family: Geneva, Arial, Helvetica, sans-serif;
            font-weight:bold;
            color:#05B;
            font-size: 1.2em; 
            letter-spacing:.1em;
            line-height:.2em;
            padding:20px auto;
            }
            
      .itinerary A:link , .itinerary A:visited {
            text-decoration:none;
            color:#000;
            margin-top:3em;
            margin-left:5px;
            padding: 0;
            font-size: 13px;
            font-family: Verdana, Arial, Helvetica, sans-serif;
            padding:3px;}
      
      .itinerary A:hover {
            text-decoration:none;
            background: #96B9D7;
            } 
      -->
   </style>
   <link href="/static/style_sheet.css" rel="stylesheet" type="text/css">
   <link REL="stylesheet" HREF="/static/style_imscart.css" TYPE="text/css">

   <style type="text/css">
      <!--
      .style12 {color: #990033}
      -->
   </style>


<table>
<tr><td style="vertical-align:top;margin-left:25px;" align=center bgcolor=white>
    <br>
      
         
            
               
                  <div align=left>
                     <h3>Pending Requests for Reseller</h3>
                     <div style="margin-left:15px;">
                        <br>
                        <table width=100%>
                           
                           </tr></table>

                     </div>
                  </div><br>
                  <hr>
               
            
         
      
       <table width=100%><tr><td>
         <div align=left>
            <h2>Current resellers</h2>
         </div>
      </td>

      <td align=right>
         
            
            
               <table><tr><td><B>KEY:</B></td><td><table><tr><td>Reg Reseller</td><td><div style="width:15px;background-color:#78e89a;">&nbsp;&nbsp;&nbsp;&nbsp;</div></td></tr></table></td><td><table><tr><td>CC Reseller</td><td><div style="width:15px;background-color:#abb3fb;">&nbsp;&nbsp;&nbsp;&nbsp;</div></td></tr></table></td><td><table><tr><td>Pow Wow</td><td><div style="width:15px;background-color:#f4b3c5;">&nbsp;&nbsp;&nbsp;&nbsp;</div></td></tr></table></td><td><table><tr><td>Travel Agent</td><td><div style="width:15px;background-color:#e7f981;">&nbsp;&nbsp;&nbsp;&nbsp;</div></td></tr></table></td><td><table><tr><td>Admin</td><td><div style="width:15px;background-color:#d7d1d1;">&nbsp;&nbsp;&nbsp;&nbsp;</div></td></tr></table></td><td><table><tr><td>Couponing</td><td><div style="width:15px;background-color:#f6b490;">&nbsp;&nbsp;&nbsp;&nbsp;</div></td></tr></table></td></tr></table>
            <br>
            <a style="font-face:Verdana;font-size:9pt;" href="javascript:void(0);" onclick="$('#addcategory').toggle();">Add category</a>
            <a style="font-face:Verdana;font-size:9pt;" href="javascript:void(0);" onclick="$('#delcategory').toggle();">Del category</a>

            <div id=delcategory style="border:1px solid black;width:300px;">
               <div align=center>Category name:</div>
               <div style="margin-left:10px;" align=right>
                  
                     <table width=200px;><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;
                     </div></td><td><a href="/affiliates?delcat=Couponing">Couponing</a></td></tr></table>
                  
                     <table width=200px;><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;
                     </div></td><td><a href="/affiliates?delcat=CC Reseller">CC Reseller</a></td></tr></table>

                  
                     <table width=200px;><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;
                     </div></td><td><a href="/affiliates?delcat=Reg Reseller">Reg Reseller</a></td></tr></table>
                  
                     <table width=200px;><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;
                     </div></td><td><a href="/affiliates?delcat=Pow Wow">Pow Wow</a></td></tr></table>
                  
                     <table width=200px;><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;
                     </div></td><td><a href="/affiliates?delcat=Travel Agent">Travel Agent</a></td></tr></table>
                  
                     <table width=200px;><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;

                     </div></td><td><a href="/affiliates?delcat=Admin">Admin</a></td></tr></table>
                  
               </div>
            </div>
            <div id=addcategory align=left style="border:1px solid black;width:600px;"><br>
               <center><form action="/affiliates" method=GET>
                  <table><tr><td>Category name: (no spaces)</td>
                  <td><input type=text name=newcategory></td></tr></table>
               </form></center>

            </div>
            <script>$('#addcategory').toggle();</script>
            <script>$('#delcategory').toggle();</script>
         
      </td>
      </tr></table>
      <table width=100% style="margin-left:15px;border:1px solid grey;">
         <tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">

                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/26934>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26934').load('/show_affiliate?cid=26934');"><b><font color=#66023C></font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=83 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=0 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_83').toggle();">[info]</a>

                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/83">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_83').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_83').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26934></div>

                        <div id=showcode_83><br>0<br>  </div>
                        <div id=info_83 style="font-size:7pt;">
					<a href=/admin/auth/user/387>user</a> | 
					<a href=/admin/contact/contact/26934>contact</a> | 
					<a href=/admin/reseller/reseller/83>reseller</a> | 
					<a href=/admin/auth/user/387/password>password</a> | 
			</div>

                        <div id=addcat_83>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=83">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=83">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=83">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=83">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=83">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=83">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=83">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_83').toggle();
				$('#addcat_83').toggle();
				$('#info_83').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#f6b490;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/92>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_92').load('/show_affiliate?cid=92');"><b><font color=#66023C>$3 Off Link</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=18 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=2300746480603769503 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_18').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 9.1
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/18">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_18').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_18').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_92></div>
                        <div id=showcode_18><br>2300746480603769503<br>  </div>
                        <div id=info_18 style="font-size:7pt;">
					<a href=/admin/auth/user/23>user</a> | 
					<a href=/admin/contact/contact/92>contact</a> | 
					<a href=/admin/reseller/reseller/18>reseller</a> | 
					<a href=/admin/auth/user/23/password>password</a> | 
			</div>

                        <div id=addcat_18>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Couponing)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=18">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=18">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=18">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=18">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=18">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=18">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=18">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_18').toggle();
				$('#addcat_18').toggle();
				$('#info_18').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#f6b490;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/620>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_620').load('/show_affiliate?cid=620');"><b><font color=#66023C>$5 Off Wine Country</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=21 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5057703601368111820 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_21').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 5.5
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/21">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_21').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_21').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_620></div>
                        <div id=showcode_21><br>5057703601368111820<br>  </div>
                        <div id=info_21 style="font-size:7pt;">
					<a href=/admin/auth/user/26>user</a> | 
					<a href=/admin/contact/contact/620>contact</a> | 
					<a href=/admin/reseller/reseller/21>reseller</a> | 
					<a href=/admin/auth/user/26/password>password</a> | 
			</div>

                        <div id=addcat_21>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Couponing)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=21">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=21">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=21">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=21">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=21">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=21">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=21">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_21').toggle();
				$('#addcat_21').toggle();
				$('#info_21').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/27965>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_27965').load('/show_affiliate?cid=27965');"><b><font color=#66023C>A Friend In Town</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=92 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5561951302791748932 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_92').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/92">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_92').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_92').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_27965></div>
                        <div id=showcode_92><br>5561951302791748932<br>  </div>
                        <div id=info_92 style="font-size:7pt;">
					<a href=/admin/auth/user/391>user</a> | 
					<a href=/admin/contact/contact/27965>contact</a> | 
					<a href=/admin/reseller/reseller/92>reseller</a> | 
					<a href=/admin/auth/user/391/password>password</a> | 
			</div>

                        <div id=addcat_92>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=92">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=92">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=92">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=92">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=92">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=92">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=92">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_92').toggle();
				$('#addcat_92').toggle();
				$('#info_92').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/26935>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26935').load('/show_affiliate?cid=26935');"><b><font color=#66023C>Aaa Allied Group</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=84 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5198685273166145199 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_84').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/84">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_84').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_84').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26935></div>
                        <div id=showcode_84><br>-5198685273166145199<br>  </div>

                        <div id=info_84 style="font-size:7pt;">
					<a href=/admin/auth/user/388>user</a> | 
					<a href=/admin/contact/contact/26935>contact</a> | 
					<a href=/admin/reseller/reseller/84>reseller</a> | 
					<a href=/admin/auth/user/388/password>password</a> | 
			</div>
                        <div id=addcat_84>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=84">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=84">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=84">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=84">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=84">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=84">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=84">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_84').toggle();
				$('#addcat_84').toggle();
				$('#info_84').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/19922>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_19922').load('/show_affiliate?cid=19922');"><b><font color=#66023C>Aaa Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=69 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7442502851205408379 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_69').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/69">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_69').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_69').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_19922></div>
                        <div id=showcode_69><br>7442502851205408379<br>  </div>
                        <div id=info_69 style="font-size:7pt;">
					<a href=/admin/auth/user/265>user</a> | 
					<a href=/admin/contact/contact/19922>contact</a> | 
					<a href=/admin/reseller/reseller/69>reseller</a> | 
					<a href=/admin/auth/user/265/password>password</a> | 
			</div>

                        <div id=addcat_69>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=69">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=69">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=69">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=69">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=69">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=69">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=69">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_69').toggle();
				$('#addcat_69').toggle();
				$('#info_69').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#78e89a;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/7070>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_7070').load('/show_affiliate?cid=7070');"><b><font color=#66023C>Ad Solution</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=38 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2941681484418238749 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_38').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/38">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_38').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_38').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_7070></div>
                        <div id=showcode_38><br>-2941681484418238749<br>  </div>
                        <div id=info_38 style="font-size:7pt;">
					<a href=/admin/auth/user/140>user</a> | 
					<a href=/admin/contact/contact/7070>contact</a> | 
					<a href=/admin/reseller/reseller/38>reseller</a> | 
					<a href=/admin/auth/user/140/password>password</a> | 
			</div>

                        <div id=addcat_38>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Reg Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=38">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=38">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=38">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=38">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=38">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=38">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=38">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_38').toggle();
				$('#addcat_38').toggle();
				$('#info_38').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/11087>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_11087').load('/show_affiliate?cid=11087');"><b><font color=#66023C>Ada Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=45 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=3215576445909023218 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_45').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/45">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_45').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_45').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_11087></div>
                        <div id=showcode_45><br>3215576445909023218<br>  </div>
                        <div id=info_45 style="font-size:7pt;">
					<a href=/admin/auth/user/187>user</a> | 
					<a href=/admin/contact/contact/11087>contact</a> | 
					<a href=/admin/reseller/reseller/45>reseller</a> | 
					<a href=/admin/auth/user/187/password>password</a> | 
			</div>

                        <div id=addcat_45>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=45">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=45">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=45">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=45">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=45">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=45">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=45">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_45').toggle();
				$('#addcat_45').toggle();
				$('#info_45').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/29863>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_29863').load('/show_affiliate?cid=29863');"><b><font color=#66023C>Adler Travel Agency</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=96 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7549446540360230066 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_96').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        28.3 / 0
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/96">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_96').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_96').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_29863></div>
                        <div id=showcode_96><br>7549446540360230066<br>  </div>

                        <div id=info_96 style="font-size:7pt;">
					<a href=/admin/auth/user/433>user</a> | 
					<a href=/admin/contact/contact/29863>contact</a> | 
					<a href=/admin/reseller/reseller/96>reseller</a> | 
					<a href=/admin/auth/user/433/password>password</a> | 
			</div>
                        <div id=addcat_96>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=96">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=96">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=96">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=96">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=96">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=96">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=96">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_96').toggle();
				$('#addcat_96').toggle();
				$('#info_96').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/19748>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_19748').load('/show_affiliate?cid=19748');"><b><font color=#66023C>Adventures In Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=68 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5353062351909093660 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_68').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/68">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_68').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_68').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_19748></div>
                        <div id=showcode_68><br>-5353062351909093660<br>  </div>
                        <div id=info_68 style="font-size:7pt;">
					<a href=/admin/auth/user/263>user</a> | 
					<a href=/admin/contact/contact/19748>contact</a> | 
					<a href=/admin/reseller/reseller/68>reseller</a> | 
					<a href=/admin/auth/user/263/password>password</a> | 
			</div>

                        <div id=addcat_68>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=68">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=68">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=68">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=68">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=68">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=68">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=68">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_68').toggle();
				$('#addcat_68').toggle();
				$('#info_68').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/35159>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_35159').load('/show_affiliate?cid=35159');"><b><font color=#66023C>Akquasunholidays</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=114 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5397448818597100552 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_114').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/114">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_114').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_114').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_35159></div>
                        <div id=showcode_114><br>5397448818597100552<br>  </div>
                        <div id=info_114 style="font-size:7pt;">
					<a href=/admin/auth/user/494>user</a> | 
					<a href=/admin/contact/contact/35159>contact</a> | 
					<a href=/admin/reseller/reseller/114>reseller</a> | 
					<a href=/admin/auth/user/494/password>password</a> | 
			</div>

                        <div id=addcat_114>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=114">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=114">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=114">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=114">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=114">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=114">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=114">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_114').toggle();
				$('#addcat_114').toggle();
				$('#info_114').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/9194>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_9194').load('/show_affiliate?cid=9194');"><b><font color=#66023C>Alcatraz Media</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=43 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-112608857839656262 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_43').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>25 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/43">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_43').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_43').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_9194></div>
                        <div id=showcode_43><br>-112608857839656262<br>  </div>
                        <div id=info_43 style="font-size:7pt;">
					<a href=/admin/auth/user/169>user</a> | 
					<a href=/admin/contact/contact/9194>contact</a> | 
					<a href=/admin/reseller/reseller/43>reseller</a> | 
					<a href=/admin/auth/user/169/password>password</a> | 
			</div>

                        <div id=addcat_43>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=43">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=43">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=43">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=43">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=43">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=43">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=43">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_43').toggle();
				$('#addcat_43').toggle();
				$('#info_43').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/15221>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_15221').load('/show_affiliate?cid=15221');"><b><font color=#66023C>Alliedtpro</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=54 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-4117934038424191130 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_54').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/54">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_54').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_54').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_15221></div>
                        <div id=showcode_54><br>-4117934038424191130<br>  </div>

                        <div id=info_54 style="font-size:7pt;">
					<a href=/admin/auth/user/222>user</a> | 
					<a href=/admin/contact/contact/15221>contact</a> | 
					<a href=/admin/reseller/reseller/54>reseller</a> | 
					<a href=/admin/auth/user/222/password>password</a> | 
			</div>
                        <div id=addcat_54>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=54">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=54">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=54">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=54">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=54">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=54">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=54">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_54').toggle();
				$('#addcat_54').toggle();
				$('#info_54').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#78e89a;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/5111>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_5111').load('/show_affiliate?cid=5111');"><b><font color=#66023C>America Viaggi Inc</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=32 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2446768643788897455 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_32').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/32">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_32').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_32').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_5111></div>
                        <div id=showcode_32><br>-2446768643788897455<br>  </div>
                        <div id=info_32 style="font-size:7pt;">
					<a href=/admin/auth/user/71>user</a> | 
					<a href=/admin/contact/contact/5111>contact</a> | 
					<a href=/admin/reseller/reseller/32>reseller</a> | 
					<a href=/admin/auth/user/71/password>password</a> | 
			</div>

                        <div id=addcat_32>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Reg Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=32">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=32">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=32">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=32">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=32">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=32">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=32">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_32').toggle();
				$('#addcat_32').toggle();
				$('#info_32').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/33751>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_33751').load('/show_affiliate?cid=33751');"><b><font color=#66023C>American Cruise &amp; Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=111 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-4746786472565761021 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_111').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/111">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_111').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_111').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_33751></div>
                        <div id=showcode_111><br>-4746786472565761021<br>  </div>
                        <div id=info_111 style="font-size:7pt;">
					<a href=/admin/auth/user/481>user</a> | 
					<a href=/admin/contact/contact/33751>contact</a> | 
					<a href=/admin/reseller/reseller/111>reseller</a> | 
					<a href=/admin/auth/user/481/password>password</a> | 
			</div>

                        <div id=addcat_111>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=111">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=111">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=111">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=111">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=111">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=111">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=111">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_111').toggle();
				$('#addcat_111').toggle();
				$('#info_111').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/19262>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_19262').load('/show_affiliate?cid=19262');"><b><font color=#66023C>Ares (City Tour &amp; Muir Woods)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=64 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7578939539857827809 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_64').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>25 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/64">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_64').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_64').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_19262></div>
                        <div id=showcode_64><br>-7578939539857827809<br>  </div>
                        <div id=info_64 style="font-size:7pt;">
					<a href=/admin/auth/user/257>user</a> | 
					<a href=/admin/contact/contact/19262>contact</a> | 
					<a href=/admin/reseller/reseller/64>reseller</a> | 
					<a href=/admin/auth/user/257/password>password</a> | 
			</div>

                        <div id=addcat_64>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=64">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=64">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=64">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=64">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=64">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=64">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=64">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_64').toggle();
				$('#addcat_64').toggle();
				$('#info_64').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/5>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_5').load('/show_affiliate?cid=5');"><b><font color=#66023C>Ares (Wine Country)</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=3 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7005334151574858034 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_3').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>25 / 0</font>

                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/3">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_3').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_3').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_5></div>
                        <div id=showcode_3><br>-7005334151574858034<br>  </div>

                        <div id=info_3 style="font-size:7pt;">
					<a href=/admin/auth/user/3>user</a> | 
					<a href=/admin/contact/contact/5>contact</a> | 
					<a href=/admin/reseller/reseller/3>reseller</a> | 
					<a href=/admin/auth/user/3/password>password</a> | 
			</div>
                        <div id=addcat_3>

                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=3">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=3">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=3">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=3">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=3">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=3">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=3">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_3').toggle();
				$('#addcat_3').toggle();
				$('#info_3').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/27563>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_27563').load('/show_affiliate?cid=27563');"><b><font color=#66023C>Avenues To Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=89 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2037217001950487279 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_89').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/89">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_89').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_89').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_27563></div>
                        <div id=showcode_89><br>-2037217001950487279<br>  </div>
                        <div id=info_89 style="font-size:7pt;">
					<a href=/admin/auth/user/390>user</a> | 
					<a href=/admin/contact/contact/27563>contact</a> | 
					<a href=/admin/reseller/reseller/89>reseller</a> | 
					<a href=/admin/auth/user/390/password>password</a> | 
			</div>

                        <div id=addcat_89>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=89">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=89">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=89">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=89">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=89">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=89">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=89">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_89').toggle();
				$('#addcat_89').toggle();
				$('#info_89').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#f6b490;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/111>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_111').load('/show_affiliate?cid=111');"><b><font color=#66023C>Brenneman Travel Store</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=19 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2819986131190860097 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_19').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/19">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_19').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_19').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_111></div>
                        <div id=showcode_19><br>-2819986131190860097<br>  </div>
                        <div id=info_19 style="font-size:7pt;">
					<a href=/admin/auth/user/24>user</a> | 
					<a href=/admin/contact/contact/111>contact</a> | 
					<a href=/admin/reseller/reseller/19>reseller</a> | 
					<a href=/admin/auth/user/24/password>password</a> | 
			</div>

                        <div id=addcat_19>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Couponing)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=19">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=19">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=19">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=19">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=19">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=19">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=19">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_19').toggle();
				$('#addcat_19').toggle();
				$('#info_19').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/6631>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_6631').load('/show_affiliate?cid=6631');"><b><font color=#66023C>Coral Sands Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=35 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5228624743958750948 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_35').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/35">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_35').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_35').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_6631></div>
                        <div id=showcode_35><br>5228624743958750948<br>  </div>
                        <div id=info_35 style="font-size:7pt;">
					<a href=/admin/auth/user/131>user</a> | 
					<a href=/admin/contact/contact/6631>contact</a> | 
					<a href=/admin/reseller/reseller/35>reseller</a> | 
					<a href=/admin/auth/user/131/password>password</a> | 
			</div>

                        <div id=addcat_35>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=35">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=35">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=35">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=35">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=35">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=35">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=35">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_35').toggle();
				$('#addcat_35').toggle();
				$('#info_35').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/10952>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_10952').load('/show_affiliate?cid=10952');"><b><font color=#66023C>Corporate Vacations American Express</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=47 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5686421037154763915 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_47').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/47">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_47').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_47').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_10952></div>
                        <div id=showcode_47><br>-5686421037154763915<br>  </div>

                        <div id=info_47 style="font-size:7pt;">
					<a href=/admin/auth/user/185>user</a> | 
					<a href=/admin/contact/contact/10952>contact</a> | 
					<a href=/admin/reseller/reseller/47>reseller</a> | 
					<a href=/admin/auth/user/185/password>password</a> | 
			</div>
                        <div id=addcat_47>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=47">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=47">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=47">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=47">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=47">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=47">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=47">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_47').toggle();
				$('#addcat_47').toggle();
				$('#info_47').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#78e89a;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/4772>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_4772').load('/show_affiliate?cid=4772');"><b><font color=#66023C>Cruise Expo Inc</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=29 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=2038908007264951988 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_29').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/29">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_29').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_29').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_4772></div>
                        <div id=showcode_29><br>2038908007264951988<br>  </div>
                        <div id=info_29 style="font-size:7pt;">
					<a href=/admin/auth/user/66>user</a> | 
					<a href=/admin/contact/contact/4772>contact</a> | 
					<a href=/admin/reseller/reseller/29>reseller</a> | 
					<a href=/admin/auth/user/66/password>password</a> | 
			</div>

                        <div id=addcat_29>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Reg Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=29">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=29">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=29">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=29">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=29">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=29">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=29">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_29').toggle();
				$('#addcat_29').toggle();
				$('#info_29').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/26099>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26099').load('/show_affiliate?cid=26099');"><b><font color=#66023C>Cruise Holidays</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=78 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-6080726890599022605 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_78').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/78">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_78').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_78').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26099></div>
                        <div id=showcode_78><br>-6080726890599022605<br>  </div>
                        <div id=info_78 style="font-size:7pt;">
					<a href=/admin/auth/user/381>user</a> | 
					<a href=/admin/contact/contact/26099>contact</a> | 
					<a href=/admin/reseller/reseller/78>reseller</a> | 
					<a href=/admin/auth/user/381/password>password</a> | 
			</div>

                        <div id=addcat_78>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=78">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=78">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=78">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=78">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=78">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=78">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=78">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_78').toggle();
				$('#addcat_78').toggle();
				$('#info_78').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/3981>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_3981').load('/show_affiliate?cid=3981');"><b><font color=#66023C>Cruise Holidays Of Port Coquitlam</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=28 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7150909473988249498 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_28').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/28">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_28').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_28').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_3981></div>
                        <div id=showcode_28><br>-7150909473988249498<br>  </div>
                        <div id=info_28 style="font-size:7pt;">
					<a href=/admin/auth/user/41>user</a> | 
					<a href=/admin/contact/contact/3981>contact</a> | 
					<a href=/admin/reseller/reseller/28>reseller</a> | 
					<a href=/admin/auth/user/41/password>password</a> | 
			</div>

                        <div id=addcat_28>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=28">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=28">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=28">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=28">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=28">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=28">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=28">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_28').toggle();
				$('#addcat_28').toggle();
				$('#info_28').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/22166>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_22166').load('/show_affiliate?cid=22166');"><b><font color=#66023C>Cwt Sato Travel</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=72 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7962656011189983300 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_72').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/72">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_72').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_72').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_22166></div>
                        <div id=showcode_72><br>-7962656011189983300<br>  </div>

                        <div id=info_72 style="font-size:7pt;">
					<a href=/admin/auth/user/278>user</a> | 
					<a href=/admin/contact/contact/22166>contact</a> | 
					<a href=/admin/reseller/reseller/72>reseller</a> | 
					<a href=/admin/auth/user/278/password>password</a> | 
			</div>
                        <div id=addcat_72>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=72">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=72">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=72">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=72">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=72">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=72">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=72">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_72').toggle();
				$('#addcat_72').toggle();
				$('#info_72').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/34417>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_34417').load('/show_affiliate?cid=34417');"><b><font color=#66023C>Discovery Tours &amp; Cruises</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=109 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7518789601411015376 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_109').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/109">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_109').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_109').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_34417></div>
                        <div id=showcode_109><br>7518789601411015376<br>  </div>
                        <div id=info_109 style="font-size:7pt;">
					<a href=/admin/auth/user/485>user</a> | 
					<a href=/admin/contact/contact/34417>contact</a> | 
					<a href=/admin/reseller/reseller/109>reseller</a> | 
					<a href=/admin/auth/user/485/password>password</a> | 
			</div>

                        <div id=addcat_109>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=109">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=109">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=109">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=109">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=109">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=109">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=109">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_109').toggle();
				$('#addcat_109').toggle();
				$('#info_109').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/9357>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_9357').load('/show_affiliate?cid=9357');"><b><font color=#66023C>Escape To Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=51 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=2180181175092805284 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_51').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/51">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_51').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_51').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_9357></div>
                        <div id=showcode_51><br>2180181175092805284<br>  </div>
                        <div id=info_51 style="font-size:7pt;">
					<a href=/admin/auth/user/171>user</a> | 
					<a href=/admin/contact/contact/9357>contact</a> | 
					<a href=/admin/reseller/reseller/51>reseller</a> | 
					<a href=/admin/auth/user/171/password>password</a> | 
			</div>

                        <div id=addcat_51>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=51">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=51">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=51">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=51">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=51">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=51">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=51">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_51').toggle();
				$('#addcat_51').toggle();
				$('#info_51').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/11238>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_11238').load('/show_affiliate?cid=11238');"><b><font color=#66023C>Expedia Cruiseshipcenters, Red Deer</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=44 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-6979575248803353965 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_44').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/44">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_44').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_44').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_11238></div>
                        <div id=showcode_44><br>-6979575248803353965<br>  </div>
                        <div id=info_44 style="font-size:7pt;">
					<a href=/admin/auth/user/188>user</a> | 
					<a href=/admin/contact/contact/11238>contact</a> | 
					<a href=/admin/reseller/reseller/44>reseller</a> | 
					<a href=/admin/auth/user/188/password>password</a> | 
			</div>

                        <div id=addcat_44>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=44">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=44">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=44">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=44">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=44">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=44">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=44">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_44').toggle();
				$('#addcat_44').toggle();
				$('#info_44').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/2731>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_2731').load('/show_affiliate?cid=2731');"><b><font color=#66023C>Experience Life Travel Club</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=25 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=4826604803480898473 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_25').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/25">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_25').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_25').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_2731></div>
                        <div id=showcode_25><br>4826604803480898473<br>  </div>

                        <div id=info_25 style="font-size:7pt;">
					<a href=/admin/auth/user/35>user</a> | 
					<a href=/admin/contact/contact/2731>contact</a> | 
					<a href=/admin/reseller/reseller/25>reseller</a> | 
					<a href=/admin/auth/user/35/password>password</a> | 
			</div>
                        <div id=addcat_25>

                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=25">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=25">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=25">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=25">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=25">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=25">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=25">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_25').toggle();
				$('#addcat_25').toggle();
				$('#info_25').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/25>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_25').load('/show_affiliate?cid=25');"><b><font color=#66023C>Extranomical Adventures</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=8 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-6503084221258562167 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_8').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>25 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/8">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_8').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_8').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_25></div>
                        <div id=showcode_8><br>-6503084221258562167<br>  </div>
                        <div id=info_8 style="font-size:7pt;">
					<a href=/admin/auth/user/10>user</a> | 
					<a href=/admin/contact/contact/25>contact</a> | 
					<a href=/admin/reseller/reseller/8>reseller</a> | 
					<a href=/admin/auth/user/10/password>password</a> | 
			</div>

                        <div id=addcat_8>
                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=8">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=8">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=8">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=8">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=8">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=8">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=8">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_8').toggle();
				$('#addcat_8').toggle();
				$('#info_8').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/10958>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_10958').load('/show_affiliate?cid=10958');"><b><font color=#66023C>Ferris Travel Service</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=46 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-8837884605674001987 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_46').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/46">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_46').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_46').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_10958></div>
                        <div id=showcode_46><br>-8837884605674001987<br>  </div>
                        <div id=info_46 style="font-size:7pt;">
					<a href=/admin/auth/user/186>user</a> | 
					<a href=/admin/contact/contact/10958>contact</a> | 
					<a href=/admin/reseller/reseller/46>reseller</a> | 
					<a href=/admin/auth/user/186/password>password</a> | 
			</div>

                        <div id=addcat_46>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=46">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=46">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=46">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=46">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=46">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=46">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=46">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_46').toggle();
				$('#addcat_46').toggle();
				$('#info_46').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/34686>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_34686').load('/show_affiliate?cid=34686');"><b><font color=#66023C>First Class Connection</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=110 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2741673328535281288 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_110').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/110">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_110').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_110').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_34686></div>
                        <div id=showcode_110><br>-2741673328535281288<br>  </div>
                        <div id=info_110 style="font-size:7pt;">
					<a href=/admin/auth/user/486>user</a> | 
					<a href=/admin/contact/contact/34686>contact</a> | 
					<a href=/admin/reseller/reseller/110>reseller</a> | 
					<a href=/admin/auth/user/486/password>password</a> | 
			</div>

                        <div id=addcat_110>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=110">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=110">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=110">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=110">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=110">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=110">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=110">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_110').toggle();
				$('#addcat_110').toggle();
				$('#info_110').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/4855>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_4855').load('/show_affiliate?cid=4855');"><b><font color=#66023C>Focus Travel</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=30 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5956554579426103160 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_30').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 21.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/30">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_30').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_30').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_4855></div>
                        <div id=showcode_30><br>5956554579426103160<br>  </div>

                        <div id=info_30 style="font-size:7pt;">
					<a href=/admin/auth/user/67>user</a> | 
					<a href=/admin/contact/contact/4855>contact</a> | 
					<a href=/admin/reseller/reseller/30>reseller</a> | 
					<a href=/admin/auth/user/67/password>password</a> | 
			</div>
                        <div id=addcat_30>

                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=30">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=30">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=30">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=30">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=30">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=30">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=30">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_30').toggle();
				$('#addcat_30').toggle();
				$('#info_30').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/28320>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_28320').load('/show_affiliate?cid=28320');"><b><font color=#66023C>Funsherpa.Com</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=86 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1687404074525321250 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_86').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/86">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_86').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_86').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_28320></div>
                        <div id=showcode_86><br>-1687404074525321250<br>  </div>
                        <div id=info_86 style="font-size:7pt;">
					<a href=/admin/auth/user/394>user</a> | 
					<a href=/admin/contact/contact/28320>contact</a> | 
					<a href=/admin/reseller/reseller/86>reseller</a> | 
					<a href=/admin/auth/user/394/password>password</a> | 
			</div>

                        <div id=addcat_86>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=86">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=86">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=86">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=86">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=86">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=86">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=86">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_86').toggle();
				$('#addcat_86').toggle();
				$('#info_86').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/18458>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_18458').load('/show_affiliate?cid=18458');"><b><font color=#66023C>Gordon Yigal Free Link</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=58 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5962562770245853755 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_58').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>0 / 100</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/58">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_58').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_58').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_18458></div>
                        <div id=showcode_58><br>-5962562770245853755<br>  </div>
                        <div id=info_58 style="font-size:7pt;">
					<a href=/admin/auth/user/245>user</a> | 
					<a href=/admin/contact/contact/18458>contact</a> | 
					<a href=/admin/reseller/reseller/58>reseller</a> | 
					<a href=/admin/auth/user/245/password>password</a> | 
			</div>

                        <div id=addcat_58>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=58">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=58">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=58">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=58">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=58">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=58">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=58">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_58').toggle();
				$('#addcat_58').toggle();
				$('#info_58').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/12439>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_12439').load('/show_affiliate?cid=12439');"><b><font color=#66023C>Hot Club Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=48 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-8347364484642269070 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_48').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/48">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_48').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_48').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_12439></div>
                        <div id=showcode_48><br>-8347364484642269070<br>  </div>
                        <div id=info_48 style="font-size:7pt;">
					<a href=/admin/auth/user/202>user</a> | 
					<a href=/admin/contact/contact/12439>contact</a> | 
					<a href=/admin/reseller/reseller/48>reseller</a> | 
					<a href=/admin/auth/user/202/password>password</a> | 
			</div>

                        <div id=addcat_48>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=48">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=48">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=48">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=48">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=48">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=48">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=48">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_48').toggle();
				$('#addcat_48').toggle();
				$('#info_48').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/29>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_29').load('/show_affiliate?cid=29');"><b><font color=#66023C>Hyatt Reg (Wine/Combo Tours)</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=10 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1488090005867312582 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_10').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>18.94 / 0</font>

                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/10">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_10').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_10').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_29></div>
                        <div id=showcode_10><br>-1488090005867312582<br>  </div>

                        <div id=info_10 style="font-size:7pt;">
					<a href=/admin/auth/user/14>user</a> | 
					<a href=/admin/contact/contact/29>contact</a> | 
					<a href=/admin/reseller/reseller/10>reseller</a> | 
					<a href=/admin/auth/user/14/password>password</a> | 
			</div>
                        <div id=addcat_10>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=10">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=10">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=10">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=10">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=10">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=10">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=10">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_10').toggle();
				$('#addcat_10').toggle();
				$('#info_10').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/30>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_30').load('/show_affiliate?cid=30');"><b><font color=#66023C>Hyatt Reg (Wkd Wine Tours)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=11 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-6325168755310255325 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_11').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        18.94 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/11">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_11').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_11').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_30></div>
                        <div id=showcode_11><br>-6325168755310255325<br>  </div>
                        <div id=info_11 style="font-size:7pt;">
					<a href=/admin/auth/user/15>user</a> | 
					<a href=/admin/contact/contact/30>contact</a> | 
					<a href=/admin/reseller/reseller/11>reseller</a> | 
					<a href=/admin/auth/user/15/password>password</a> | 
			</div>

                        <div id=addcat_11>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=11">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=11">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=11">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=11">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=11">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=11">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=11">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_11').toggle();
				$('#addcat_11').toggle();
				$('#info_11').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/28>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_28').load('/show_affiliate?cid=28');"><b><font color=#66023C>Hyatt Regency (City/Muir)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=9 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7525430533770938236 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_9').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>23.8 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/9">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_9').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_9').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_28></div>
                        <div id=showcode_9><br>7525430533770938236<br>  </div>
                        <div id=info_9 style="font-size:7pt;">
					<a href=/admin/auth/user/13>user</a> | 
					<a href=/admin/contact/contact/28>contact</a> | 
					<a href=/admin/reseller/reseller/9>reseller</a> | 
					<a href=/admin/auth/user/13/password>password</a> | 
			</div>

                        <div id=addcat_9>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=9">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=9">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=9">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=9">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=9">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=9">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=9">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_9').toggle();
				$('#addcat_9').toggle();
				$('#info_9').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#78e89a;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/21>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_21').load('/show_affiliate?cid=21');"><b><font color=#66023C>Illusion Industries</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=12 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-3034464430223973002 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_12').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        20 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/12">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_12').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_12').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_21></div>
                        <div id=showcode_12><br>-3034464430223973002<br>  </div>
                        <div id=info_12 style="font-size:7pt;">
					<a href=/admin/auth/user/7>user</a> | 
					<a href=/admin/contact/contact/21>contact</a> | 
					<a href=/admin/reseller/reseller/12>reseller</a> | 
					<a href=/admin/auth/user/7/password>password</a> | 
			</div>

                        <div id=addcat_12>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Reg Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=12">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=12">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=12">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=12">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=12">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=12">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=12">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_12').toggle();
				$('#addcat_12').toggle();
				$('#info_12').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/19919>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_19919').load('/show_affiliate?cid=19919');"><b><font color=#66023C>Ingo Trans</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=67 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5932947807209881707 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_67').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/67">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_67').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_67').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_19919></div>
                        <div id=showcode_67><br>5932947807209881707<br>  </div>

                        <div id=info_67 style="font-size:7pt;">
					<a href=/admin/auth/user/264>user</a> | 
					<a href=/admin/contact/contact/19919>contact</a> | 
					<a href=/admin/reseller/reseller/67>reseller</a> | 
					<a href=/admin/auth/user/264/password>password</a> | 
			</div>
                        <div id=addcat_67>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=67">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=67">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=67">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=67">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=67">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=67">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=67">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_67').toggle();
				$('#addcat_67').toggle();
				$('#info_67').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/32592>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_32592').load('/show_affiliate?cid=32592');"><b><font color=#66023C>Internet Travel Center</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=108 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5897272772870805126 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_108').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/108">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_108').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_108').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_32592></div>
                        <div id=showcode_108><br>5897272772870805126<br>  </div>
                        <div id=info_108 style="font-size:7pt;">
					<a href=/admin/auth/user/468>user</a> | 
					<a href=/admin/contact/contact/32592>contact</a> | 
					<a href=/admin/reseller/reseller/108>reseller</a> | 
					<a href=/admin/auth/user/468/password>password</a> | 
			</div>

                        <div id=addcat_108>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=108">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=108">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=108">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=108">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=108">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=108">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=108">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_108').toggle();
				$('#addcat_108').toggle();
				$('#info_108').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/20989>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_20989').load('/show_affiliate?cid=20989');"><b><font color=#66023C>Ivymedia Corp/Gotobus</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=71 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7708817387055529773 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_71').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>25 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/71">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_71').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_71').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_20989></div>
                        <div id=showcode_71><br>-7708817387055529773<br>  </div>
                        <div id=info_71 style="font-size:7pt;">
					<a href=/admin/auth/user/270>user</a> | 
					<a href=/admin/contact/contact/20989>contact</a> | 
					<a href=/admin/reseller/reseller/71>reseller</a> | 
					<a href=/admin/auth/user/270/password>password</a> | 
			</div>

                        <div id=addcat_71>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=71">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=71">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=71">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=71">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=71">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=71">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=71">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_71').toggle();
				$('#addcat_71').toggle();
				$('#info_71').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/33101>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_33101').load('/show_affiliate?cid=33101');"><b><font color=#66023C>Jbs Group</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=106 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=457497526940538587 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_106').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/106">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_106').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_106').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_33101></div>
                        <div id=showcode_106><br>457497526940538587<br>  </div>
                        <div id=info_106 style="font-size:7pt;">
					<a href=/admin/auth/user/476>user</a> | 
					<a href=/admin/contact/contact/33101>contact</a> | 
					<a href=/admin/reseller/reseller/106>reseller</a> | 
					<a href=/admin/auth/user/476/password>password</a> | 
			</div>

                        <div id=addcat_106>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=106">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=106">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=106">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=106">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=106">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=106">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=106">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_106').toggle();
				$('#addcat_106').toggle();
				$('#info_106').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/3461>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_3461').load('/show_affiliate?cid=3461');"><b><font color=#66023C>Jules Travel Center</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=26 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2888738985158073951 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_26').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/26">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_26').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_26').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_3461></div>
                        <div id=showcode_26><br>-2888738985158073951<br>  </div>

                        <div id=info_26 style="font-size:7pt;">
					<a href=/admin/auth/user/39>user</a> | 
					<a href=/admin/contact/contact/3461>contact</a> | 
					<a href=/admin/reseller/reseller/26>reseller</a> | 
					<a href=/admin/auth/user/39/password>password</a> | 
			</div>
                        <div id=addcat_26>

                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=26">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=26">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=26">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=26">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=26">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=26">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=26">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_26').toggle();
				$('#addcat_26').toggle();
				$('#info_26').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/16355>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_16355').load('/show_affiliate?cid=16355');"><b><font color=#66023C>Just Spas &amp; Adventures</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=55 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1814578898690043258 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_55').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/55">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_55').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_55').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_16355></div>
                        <div id=showcode_55><br>-1814578898690043258<br>  </div>
                        <div id=info_55 style="font-size:7pt;">
					<a href=/admin/auth/user/232>user</a> | 
					<a href=/admin/contact/contact/16355>contact</a> | 
					<a href=/admin/reseller/reseller/55>reseller</a> | 
					<a href=/admin/auth/user/232/password>password</a> | 
			</div>

                        <div id=addcat_55>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=55">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=55">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=55">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=55">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=55">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=55">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=55">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_55').toggle();
				$('#addcat_55').toggle();
				$('#info_55').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/26951>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26951').load('/show_affiliate?cid=26951');"><b><font color=#66023C>Koch Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=93 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7260791589809261602 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_93').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        15 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/93">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_93').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_93').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26951></div>
                        <div id=showcode_93><br>-7260791589809261602<br>  </div>
                        <div id=info_93 style="font-size:7pt;">
					<a href=/admin/auth/user/389>user</a> | 
					<a href=/admin/contact/contact/26951>contact</a> | 
					<a href=/admin/reseller/reseller/93>reseller</a> | 
					<a href=/admin/auth/user/389/password>password</a> | 
			</div>

                        <div id=addcat_93>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=93">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=93">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=93">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=93">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=93">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=93">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=93">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_93').toggle();
				$('#addcat_93').toggle();
				$('#info_93').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/4585>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_4585').load('/show_affiliate?cid=4585');"><b><font color=#66023C>Largay Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=31 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=6742598987060556679 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_31').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/31">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_31').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_31').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_4585></div>
                        <div id=showcode_31><br>6742598987060556679<br>  </div>
                        <div id=info_31 style="font-size:7pt;">
					<a href=/admin/auth/user/58>user</a> | 
					<a href=/admin/contact/contact/4585>contact</a> | 
					<a href=/admin/reseller/reseller/31>reseller</a> | 
					<a href=/admin/auth/user/58/password>password</a> | 
			</div>

                        <div id=addcat_31>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=31">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=31">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=31">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=31">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=31">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=31">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=31">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_31').toggle();
				$('#addcat_31').toggle();
				$('#info_31').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/33028>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_33028').load('/show_affiliate?cid=33028');"><b><font color=#66023C>Lighthouse Travel &amp; Tours</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=107 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=6529552060823798694 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_107').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;

                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/107">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_107').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_107').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_33028></div>
                        <div id=showcode_107><br>6529552060823798694<br>  </div>

                        <div id=info_107 style="font-size:7pt;">
					<a href=/admin/auth/user/475>user</a> | 
					<a href=/admin/contact/contact/33028>contact</a> | 
					<a href=/admin/reseller/reseller/107>reseller</a> | 
					<a href=/admin/auth/user/475/password>password</a> | 
			</div>
                        <div id=addcat_107>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=107">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=107">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=107">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=107">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=107">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=107">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=107">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_107').toggle();
				$('#addcat_107').toggle();
				$('#info_107').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/691>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_691').load('/show_affiliate?cid=691');"><b><font color=#66023C>Lobstick Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=23 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=700206154285052680 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_23').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / -23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/23">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_23').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_23').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_691></div>
                        <div id=showcode_23><br>700206154285052680<br>  </div>
                        <div id=info_23 style="font-size:7pt;">
					<a href=/admin/auth/user/29>user</a> | 
					<a href=/admin/contact/contact/691>contact</a> | 
					<a href=/admin/reseller/reseller/23>reseller</a> | 
					<a href=/admin/auth/user/29/password>password</a> | 
			</div>

                        <div id=addcat_23>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=23">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=23">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=23">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=23">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=23">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=23">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=23">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_23').toggle();
				$('#addcat_23').toggle();
				$('#info_23').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/43>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_43').load('/show_affiliate?cid=43');"><b><font color=#66023C>Look Tours (City Tour)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=16 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1423124472667321264 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_16').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>29.02 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/16">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_16').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_16').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_43></div>
                        <div id=showcode_16><br>-1423124472667321264<br>  </div>
                        <div id=info_16 style="font-size:7pt;">
					<a href=/admin/auth/user/20>user</a> | 
					<a href=/admin/contact/contact/43>contact</a> | 
					<a href=/admin/reseller/reseller/16>reseller</a> | 
					<a href=/admin/auth/user/20/password>password</a> | 
			</div>

                        <div id=addcat_16>
                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=16">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=16">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=16">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=16">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=16">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=16">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=16">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_16').toggle();
				$('#addcat_16').toggle();
				$('#info_16').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/44>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_44').load('/show_affiliate?cid=44');"><b><font color=#66023C>Look Tours (Muir Woods)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=15 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5024919134150510389 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_15').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>27.91 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/15">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_15').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_15').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_44></div>
                        <div id=showcode_15><br>5024919134150510389<br>  </div>
                        <div id=info_15 style="font-size:7pt;">
					<a href=/admin/auth/user/21>user</a> | 
					<a href=/admin/contact/contact/44>contact</a> | 
					<a href=/admin/reseller/reseller/15>reseller</a> | 
					<a href=/admin/auth/user/21/password>password</a> | 
			</div>

                        <div id=addcat_15>
                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=15">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=15">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=15">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=15">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=15">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=15">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=15">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_15').toggle();
				$('#addcat_15').toggle();
				$('#info_15').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/45>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_45').load('/show_affiliate?cid=45');"><b><font color=#66023C>Look Tours (Wine)</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=17 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1863985730868521715 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_17').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>29.99 / 0</font>

                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/17">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_17').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_17').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_45></div>
                        <div id=showcode_17><br>-1863985730868521715<br>  </div>

                        <div id=info_17 style="font-size:7pt;">
					<a href=/admin/auth/user/22>user</a> | 
					<a href=/admin/contact/contact/45>contact</a> | 
					<a href=/admin/reseller/reseller/17>reseller</a> | 
					<a href=/admin/auth/user/22/password>password</a> | 
			</div>
                        <div id=addcat_17>

                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=17">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=17">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=17">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=17">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=17">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=17">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=17">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_17').toggle();
				$('#addcat_17').toggle();
				$('#info_17').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/42>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_42').load('/show_affiliate?cid=42');"><b><font color=#66023C>Look Tours City Mw Combo</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=14 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=9163574257634841441 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_14').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>24 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/14">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_14').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_14').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_42></div>
                        <div id=showcode_14><br>9163574257634841441<br>  </div>
                        <div id=info_14 style="font-size:7pt;">
					<a href=/admin/auth/user/19>user</a> | 
					<a href=/admin/contact/contact/42>contact</a> | 
					<a href=/admin/reseller/reseller/14>reseller</a> | 
					<a href=/admin/auth/user/19/password>password</a> | 
			</div>

                        <div id=addcat_14>
                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=14">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=14">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=14">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=14">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=14">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=14">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=14">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_14').toggle();
				$('#addcat_14').toggle();
				$('#info_14').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/7589>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_7589').load('/show_affiliate?cid=7589');"><b><font color=#66023C>Melody Travel &amp; Tours</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=39 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7349883611405746510 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_39').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/39">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_39').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_39').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_7589></div>
                        <div id=showcode_39><br>7349883611405746510<br>  </div>
                        <div id=info_39 style="font-size:7pt;">
					<a href=/admin/auth/user/146>user</a> | 
					<a href=/admin/contact/contact/7589>contact</a> | 
					<a href=/admin/reseller/reseller/39>reseller</a> | 
					<a href=/admin/auth/user/146/password>password</a> | 
			</div>

                        <div id=addcat_39>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=39">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=39">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=39">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=39">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=39">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=39">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=39">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_39').toggle();
				$('#addcat_39').toggle();
				$('#info_39').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/30795>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_30795').load('/show_affiliate?cid=30795');"><b><font color=#66023C>Messe Reps. &amp; Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=98 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-3373851494205387793 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_98').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/98">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_98').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_98').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_30795></div>
                        <div id=showcode_98><br>-3373851494205387793<br>  </div>
                        <div id=info_98 style="font-size:7pt;">
					<a href=/admin/auth/user/443>user</a> | 
					<a href=/admin/contact/contact/30795>contact</a> | 
					<a href=/admin/reseller/reseller/98>reseller</a> | 
					<a href=/admin/auth/user/443/password>password</a> | 
			</div>

                        <div id=addcat_98>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=98">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=98">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=98">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=98">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=98">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=98">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=98">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_98').toggle();
				$('#addcat_98').toggle();
				$('#info_98').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/17963>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_17963').load('/show_affiliate?cid=17963');"><b><font color=#66023C>Mind Body Tours</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=59 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5428735043653184954 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_59').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/59">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_59').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_59').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_17963></div>
                        <div id=showcode_59><br>5428735043653184954<br>  </div>

                        <div id=info_59 style="font-size:7pt;">
					<a href=/admin/auth/user/242>user</a> | 
					<a href=/admin/contact/contact/17963>contact</a> | 
					<a href=/admin/reseller/reseller/59>reseller</a> | 
					<a href=/admin/auth/user/242/password>password</a> | 
			</div>
                        <div id=addcat_59>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=59">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=59">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=59">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=59">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=59">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=59">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=59">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_59').toggle();
				$('#addcat_59').toggle();
				$('#info_59').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#78e89a;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/7012>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_7012').load('/show_affiliate?cid=7012');"><b><font color=#66023C>Moser Reisen Gmbh</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=36 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-8769231037732534289 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_36').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/36">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_36').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_36').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_7012></div>
                        <div id=showcode_36><br>-8769231037732534289<br>  </div>
                        <div id=info_36 style="font-size:7pt;">
					<a href=/admin/auth/user/138>user</a> | 
					<a href=/admin/contact/contact/7012>contact</a> | 
					<a href=/admin/reseller/reseller/36>reseller</a> | 
					<a href=/admin/auth/user/138/password>password</a> | 
			</div>

                        <div id=addcat_36>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Reg Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=36">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=36">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=36">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=36">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=36">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=36">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=36">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_36').toggle();
				$('#addcat_36').toggle();
				$('#info_36').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/28022>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_28022').load('/show_affiliate?cid=28022');"><b><font color=#66023C>Naka&#39;s Travel Service</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=88 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1335143504296170033 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_88').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/88">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_88').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_88').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_28022></div>
                        <div id=showcode_88><br>-1335143504296170033<br>  </div>
                        <div id=info_88 style="font-size:7pt;">
					<a href=/admin/auth/user/393>user</a> | 
					<a href=/admin/contact/contact/28022>contact</a> | 
					<a href=/admin/reseller/reseller/88>reseller</a> | 
					<a href=/admin/auth/user/393/password>password</a> | 
			</div>

                        <div id=addcat_88>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=88">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=88">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=88">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=88">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=88">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=88">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=88">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_88').toggle();
				$('#addcat_88').toggle();
				$('#info_88').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/14506>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_14506').load('/show_affiliate?cid=14506');"><b><font color=#66023C>Oracle (City/Muir Woods)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=52 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-3311281395348596008 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_52').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 7.7
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/52">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_52').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_52').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_14506></div>
                        <div id=showcode_52><br>-3311281395348596008<br>  </div>
                        <div id=info_52 style="font-size:7pt;">
					<a href=/admin/auth/user/216>user</a> | 
					<a href=/admin/contact/contact/14506>contact</a> | 
					<a href=/admin/reseller/reseller/52>reseller</a> | 
					<a href=/admin/auth/user/216/password>password</a> | 
			</div>

                        <div id=addcat_52>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=52">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=52">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=52">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=52">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=52">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=52">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=52">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_52').toggle();
				$('#addcat_52').toggle();
				$('#info_52').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/14509>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_14509').load('/show_affiliate?cid=14509');"><b><font color=#66023C>Oracle Openworld</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=53 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-1988004426092339210 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_53').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 5.5
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/53">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_53').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_53').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_14509></div>
                        <div id=showcode_53><br>-1988004426092339210<br>  </div>

                        <div id=info_53 style="font-size:7pt;">
					<a href=/admin/auth/user/217>user</a> | 
					<a href=/admin/contact/contact/14509>contact</a> | 
					<a href=/admin/reseller/reseller/53>reseller</a> | 
					<a href=/admin/auth/user/217/password>password</a> | 
			</div>
                        <div id=addcat_53>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=53">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=53">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=53">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=53">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=53">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=53">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=53">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_53').toggle();
				$('#addcat_53').toggle();
				$('#info_53').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/23319>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_23319').load('/show_affiliate?cid=23319');"><b><font color=#66023C>Ozarks&#39; Kirkwood Tour &amp; Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=75 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7942685225566134821 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_75').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/75">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_75').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_75').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_23319></div>
                        <div id=showcode_75><br>7942685225566134821<br>  </div>
                        <div id=info_75 style="font-size:7pt;">
					<a href=/admin/auth/user/299>user</a> | 
					<a href=/admin/contact/contact/23319>contact</a> | 
					<a href=/admin/reseller/reseller/75>reseller</a> | 
					<a href=/admin/auth/user/299/password>password</a> | 
			</div>

                        <div id=addcat_75>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=75">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=75">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=75">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=75">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=75">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=75">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=75">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_75').toggle();
				$('#addcat_75').toggle();
				$('#info_75').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/26326>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26326').load('/show_affiliate?cid=26326');"><b><font color=#66023C>Pinnacle Travel &amp; Tours</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=80 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=72254916889341052 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_80').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/80">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_80').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_80').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26326></div>
                        <div id=showcode_80><br>72254916889341052<br>  </div>
                        <div id=info_80 style="font-size:7pt;">
					<a href=/admin/auth/user/382>user</a> | 
					<a href=/admin/contact/contact/26326>contact</a> | 
					<a href=/admin/reseller/reseller/80>reseller</a> | 
					<a href=/admin/auth/user/382/password>password</a> | 
			</div>

                        <div id=addcat_80>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=80">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=80">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=80">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=80">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=80">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=80">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=80">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_80').toggle();
				$('#addcat_80').toggle();
				$('#info_80').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/35059>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_35059').load('/show_affiliate?cid=35059');"><b><font color=#66023C>Pkt Tours Usa, Inc</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=112 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=179829140051929713 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_112').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/112">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_112').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_112').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_35059></div>
                        <div id=showcode_112><br>179829140051929713<br>  </div>
                        <div id=info_112 style="font-size:7pt;">
					<a href=/admin/auth/user/490>user</a> | 
					<a href=/admin/contact/contact/35059>contact</a> | 
					<a href=/admin/reseller/reseller/112>reseller</a> | 
					<a href=/admin/auth/user/490/password>password</a> | 
			</div>

                        <div id=addcat_112>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=112">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=112">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=112">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=112">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=112">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=112">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=112">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_112').toggle();
				$('#addcat_112').toggle();
				$('#info_112').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/23991>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_23991').load('/show_affiliate?cid=23991');"><b><font color=#66023C>Prefer Choice Travel</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=77 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=4998882364712677473 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_77').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/77">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_77').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_77').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_23991></div>
                        <div id=showcode_77><br>4998882364712677473<br>  </div>

                        <div id=info_77 style="font-size:7pt;">
					<a href=/admin/auth/user/311>user</a> | 
					<a href=/admin/contact/contact/23991>contact</a> | 
					<a href=/admin/reseller/reseller/77>reseller</a> | 
					<a href=/admin/auth/user/311/password>password</a> | 
			</div>
                        <div id=addcat_77>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=77">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=77">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=77">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=77">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=77">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=77">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=77">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_77').toggle();
				$('#addcat_77').toggle();
				$('#info_77').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/35104>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_35104').load('/show_affiliate?cid=35104');"><b><font color=#66023C>Premiere Global Sports</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=113 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7363019615756662877 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_113').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/113">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_113').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_113').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_35104></div>
                        <div id=showcode_113><br>7363019615756662877<br>  </div>
                        <div id=info_113 style="font-size:7pt;">
					<a href=/admin/auth/user/493>user</a> | 
					<a href=/admin/contact/contact/35104>contact</a> | 
					<a href=/admin/reseller/reseller/113>reseller</a> | 
					<a href=/admin/auth/user/493/password>password</a> | 
			</div>

                        <div id=addcat_113>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=113">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=113">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=113">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=113">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=113">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=113">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=113">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_113').toggle();
				$('#addcat_113').toggle();
				$('#info_113').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/26463>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26463').load('/show_affiliate?cid=26463');"><b><font color=#66023C>Prestige Accommodations</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=81 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-8720821069884432231 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_81').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        20 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/81">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_81').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_81').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26463></div>
                        <div id=showcode_81><br>-8720821069884432231<br>  </div>
                        <div id=info_81 style="font-size:7pt;">
					<a href=/admin/auth/user/383>user</a> | 
					<a href=/admin/contact/contact/26463>contact</a> | 
					<a href=/admin/reseller/reseller/81>reseller</a> | 
					<a href=/admin/auth/user/383/password>password</a> | 
			</div>

                        <div id=addcat_81>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=81">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=81">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=81">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=81">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=81">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=81">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=81">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_81').toggle();
				$('#addcat_81').toggle();
				$('#info_81').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/16487>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_16487').load('/show_affiliate?cid=16487');"><b><font color=#66023C>Prince Travel Ltd</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=61 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-490633934807115784 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_61').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/61">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_61').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_61').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_16487></div>
                        <div id=showcode_61><br>-490633934807115784<br>  </div>
                        <div id=info_61 style="font-size:7pt;">
					<a href=/admin/auth/user/234>user</a> | 
					<a href=/admin/contact/contact/16487>contact</a> | 
					<a href=/admin/reseller/reseller/61>reseller</a> | 
					<a href=/admin/auth/user/234/password>password</a> | 
			</div>

                        <div id=addcat_61>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=61">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=61">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=61">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=61">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=61">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=61">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=61">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_61').toggle();
				$('#addcat_61').toggle();
				$('#info_61').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/22970>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_22970').load('/show_affiliate?cid=22970');"><b><font color=#66023C>S&amp;V Tours, Inc</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=73 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-943384952785477600 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_73').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/73">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_73').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_73').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_22970></div>
                        <div id=showcode_73><br>-943384952785477600<br>  </div>

                        <div id=info_73 style="font-size:7pt;">
					<a href=/admin/auth/user/298>user</a> | 
					<a href=/admin/contact/contact/22970>contact</a> | 
					<a href=/admin/reseller/reseller/73>reseller</a> | 
					<a href=/admin/auth/user/298/password>password</a> | 
			</div>
                        <div id=addcat_73>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=73">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=73">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=73">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=73">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=73">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=73">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=73">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_73').toggle();
				$('#addcat_73').toggle();
				$('#info_73').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/31863>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_31863').load('/show_affiliate?cid=31863');"><b><font color=#66023C>Sait Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=101 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2261846772077576022 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_101').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        15 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/101">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_101').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_101').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_31863></div>
                        <div id=showcode_101><br>-2261846772077576022<br>  </div>
                        <div id=info_101 style="font-size:7pt;">
					<a href=/admin/auth/user/456>user</a> | 
					<a href=/admin/contact/contact/31863>contact</a> | 
					<a href=/admin/reseller/reseller/101>reseller</a> | 
					<a href=/admin/auth/user/456/password>password</a> | 
			</div>

                        <div id=addcat_101>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=101">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=101">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=101">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=101">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=101">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=101">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=101">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_101').toggle();
				$('#addcat_101').toggle();
				$('#info_101').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#f6b490;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/9>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_9').load('/show_affiliate?cid=9');"><b><font color=#66023C>Sf Shuttle Tours</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=5 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-8787242217560784383 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_5').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>0 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/5">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_5').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_5').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_9></div>
                        <div id=showcode_5><br>-8787242217560784383<br>  </div>
                        <div id=info_5 style="font-size:7pt;">
					<a href=/admin/auth/user/5>user</a> | 
					<a href=/admin/contact/contact/9>contact</a> | 
					<a href=/admin/reseller/reseller/5>reseller</a> | 
					<a href=/admin/auth/user/5/password>password</a> | 
			</div>

                        <div id=addcat_5>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Couponing)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=5">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=5">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=5">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=5">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=5">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=5">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=5">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_5').toggle();
				$('#addcat_5').toggle();
				$('#info_5').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#f6b490;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/8600>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_8600').load('/show_affiliate?cid=8600');"><b><font color=#66023C>Stratigent</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=41 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=5587630689628597975 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_41').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 100
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/41">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_41').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_41').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_8600></div>
                        <div id=showcode_41><br>5587630689628597975<br>  </div>
                        <div id=info_41 style="font-size:7pt;">
					<a href=/admin/auth/user/163>user</a> | 
					<a href=/admin/contact/contact/8600>contact</a> | 
					<a href=/admin/reseller/reseller/41>reseller</a> | 
					<a href=/admin/auth/user/163/password>password</a> | 
			</div>

                        <div id=addcat_41>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Couponing)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=41">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=41">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=41">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=41">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=41">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=41">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=41">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_41').toggle();
				$('#addcat_41').toggle();
				$('#info_41').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/19264>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_19264').load('/show_affiliate?cid=19264');"><b><font color=#66023C>Tour Corp (City Tour)</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=66 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5385242687601599847 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_66').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>20.6 / 0</font>

                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/66">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_66').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_66').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_19264></div>
                        <div id=showcode_66><br>-5385242687601599847<br>  </div>

                        <div id=info_66 style="font-size:7pt;">
					<a href=/admin/auth/user/261>user</a> | 
					<a href=/admin/contact/contact/19264>contact</a> | 
					<a href=/admin/reseller/reseller/66>reseller</a> | 
					<a href=/admin/auth/user/261/password>password</a> | 
			</div>
                        <div id=addcat_66>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=66">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=66">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=66">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=66">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=66">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=66">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=66">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_66').toggle();
				$('#addcat_66').toggle();
				$('#info_66').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/28358>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_28358').load('/show_affiliate?cid=28358');"><b><font color=#66023C>Tour Corp (Monterey)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=87 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7640993519657102388 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_87').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>20.6 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/87">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_87').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_87').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_28358></div>
                        <div id=showcode_87><br>7640993519657102388<br>  </div>
                        <div id=info_87 style="font-size:7pt;">
					<a href=/admin/auth/user/395>user</a> | 
					<a href=/admin/contact/contact/28358>contact</a> | 
					<a href=/admin/reseller/reseller/87>reseller</a> | 
					<a href=/admin/auth/user/395/password>password</a> | 
			</div>

                        <div id=addcat_87>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=87">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=87">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=87">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=87">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=87">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=87">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=87">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_87').toggle();
				$('#addcat_87').toggle();
				$('#info_87').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/6620>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_6620').load('/show_affiliate?cid=6620');"><b><font color=#66023C>Tour Corp (Winecountry)</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=33 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=4541394874649054493 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_33').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>20.6 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/33">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_33').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_33').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_6620></div>
                        <div id=showcode_33><br>4541394874649054493<br>  </div>
                        <div id=info_33 style="font-size:7pt;">
					<a href=/admin/auth/user/129>user</a> | 
					<a href=/admin/contact/contact/6620>contact</a> | 
					<a href=/admin/reseller/reseller/33>reseller</a> | 
					<a href=/admin/auth/user/129/password>password</a> | 
			</div>

                        <div id=addcat_33>
                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=33">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=33">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=33">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=33">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=33">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=33">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=33">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_33').toggle();
				$('#addcat_33').toggle();
				$('#info_33').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/24996>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_24996').load('/show_affiliate?cid=24996');"><b><font color=#66023C>Tours 4 Fun</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=76 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5760707061171938911 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_76').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>30 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/76">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_76').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_76').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_24996></div>
                        <div id=showcode_76><br>-5760707061171938911<br>  </div>
                        <div id=info_76 style="font-size:7pt;">
					<a href=/admin/auth/user/316>user</a> | 
					<a href=/admin/contact/contact/24996>contact</a> | 
					<a href=/admin/reseller/reseller/76>reseller</a> | 
					<a href=/admin/auth/user/316/password>password</a> | 
			</div>

                        <div id=addcat_76>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=76">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=76">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=76">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=76">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=76">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=76">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=76">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_76').toggle();
				$('#addcat_76').toggle();
				$('#info_76').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#78e89a;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/1844>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_1844').load('/show_affiliate?cid=1844');"><b><font color=#66023C>Tours To Boot, Inc.</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=24 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-7137467794058190787 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_24').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 18.94
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/24">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_24').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_24').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_1844></div>
                        <div id=showcode_24><br>-7137467794058190787<br>  </div>

                        <div id=info_24 style="font-size:7pt;">
					<a href=/admin/auth/user/33>user</a> | 
					<a href=/admin/contact/contact/1844>contact</a> | 
					<a href=/admin/reseller/reseller/24>reseller</a> | 
					<a href=/admin/auth/user/33/password>password</a> | 
			</div>
                        <div id=addcat_24>

                           <br>Select category: <font style="font-size:6pt;">(Currently: Reg Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=24">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=24">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=24">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=24">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=24">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=24">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=24">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_24').toggle();
				$('#addcat_24').toggle();
				$('#info_24').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/16463>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_16463').load('/show_affiliate?cid=16463');"><b><font color=#66023C>Tours4Fun</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=56 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-4229093379946357501 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_56').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 30
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/56">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_56').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_56').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_16463></div>
                        <div id=showcode_56><br>-4229093379946357501<br>  </div>
                        <div id=info_56 style="font-size:7pt;">
					<a href=/admin/auth/user/233>user</a> | 
					<a href=/admin/contact/contact/16463>contact</a> | 
					<a href=/admin/reseller/reseller/56>reseller</a> | 
					<a href=/admin/auth/user/233/password>password</a> | 
			</div>

                        <div id=addcat_56>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=56">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=56">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=56">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=56">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=56">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=56">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=56">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_56').toggle();
				$('#addcat_56').toggle();
				$('#info_56').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/7652>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_7652').load('/show_affiliate?cid=7652');"><b><font color=#66023C>Travel Masters Calgary Macleod</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=40 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=8298269053654134673 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_40').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/40">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_40').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_40').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_7652></div>
                        <div id=showcode_40><br>8298269053654134673<br>  </div>
                        <div id=info_40 style="font-size:7pt;">
					<a href=/admin/auth/user/148>user</a> | 
					<a href=/admin/contact/contact/7652>contact</a> | 
					<a href=/admin/reseller/reseller/40>reseller</a> | 
					<a href=/admin/auth/user/148/password>password</a> | 
			</div>

                        <div id=addcat_40>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=40">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=40">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=40">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=40">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=40">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=40">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=40">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_40').toggle();
				$('#addcat_40').toggle();
				$('#info_40').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#e7f981;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/3552>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_3552').load('/show_affiliate?cid=3552');"><b><font color=#66023C>Travel Planners International</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=27 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=2602032108603375910 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_27').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/27">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_27').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_27').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_3552></div>
                        <div id=showcode_27><br>2602032108603375910<br>  </div>
                        <div id=info_27 style="font-size:7pt;">
					<a href=/admin/auth/user/40>user</a> | 
					<a href=/admin/contact/contact/3552>contact</a> | 
					<a href=/admin/reseller/reseller/27>reseller</a> | 
					<a href=/admin/auth/user/40/password>password</a> | 
			</div>

                        <div id=addcat_27>
                           <br>Select category: <font style="font-size:6pt;">(Currently: Travel Agent)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=27">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=27">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=27">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=27">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=27">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=27">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=27">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_27').toggle();
				$('#addcat_27').toggle();
				$('#info_27').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/31250>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_31250').load('/show_affiliate?cid=31250');"><b><font color=#66023C>Travel Ticker 30%</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=100 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-6444614273396369919 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_100').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 30
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/100">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_100').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_100').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_31250></div>
                        <div id=showcode_100><br>-6444614273396369919<br>  </div>

                        <div id=info_100 style="font-size:7pt;">
					<a href=/admin/auth/user/448>user</a> | 
					<a href=/admin/contact/contact/31250>contact</a> | 
					<a href=/admin/reseller/reseller/100>reseller</a> | 
					<a href=/admin/auth/user/448/password>password</a> | 
			</div>
                        <div id=addcat_100>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=100">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=100">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=100">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=100">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=100">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=100">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=100">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_100').toggle();
				$('#addcat_100').toggle();
				$('#info_100').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/31248>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_31248').load('/show_affiliate?cid=31248');"><b><font color=#66023C>Travel Ticker 40%</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=99 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-6444617273382369842 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_99').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 40
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/99">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_99').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_99').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_31248></div>
                        <div id=showcode_99><br>-6444617273382369842<br>  </div>
                        <div id=info_99 style="font-size:7pt;">
					<a href=/admin/auth/user/447>user</a> | 
					<a href=/admin/contact/contact/31248>contact</a> | 
					<a href=/admin/reseller/reseller/99>reseller</a> | 
					<a href=/admin/auth/user/447/password>password</a> | 
			</div>

                        <div id=addcat_99>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=99">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=99">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=99">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=99">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=99">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=99">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=99">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_99').toggle();
				$('#addcat_99').toggle();
				$('#info_99').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/25073>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_25073').load('/show_affiliate?cid=25073');"><b><font color=#66023C>Travelscene</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=79 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=6158234476567871887 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_79').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/79">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_79').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_79').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_25073></div>
                        <div id=showcode_79><br>6158234476567871887<br>  </div>
                        <div id=info_79 style="font-size:7pt;">
					<a href=/admin/auth/user/318>user</a> | 
					<a href=/admin/contact/contact/25073>contact</a> | 
					<a href=/admin/reseller/reseller/79>reseller</a> | 
					<a href=/admin/auth/user/318/password>password</a> | 
			</div>

                        <div id=addcat_79>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=79">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=79">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=79">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=79">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=79">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=79">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=79">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_79').toggle();
				$('#addcat_79').toggle();
				$('#info_79').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/26616>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_26616').load('/show_affiliate?cid=26616');"><b><font color=#66023C>Travlbudi Llc</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=85 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=196832998539485829 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_85').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/85">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_85').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_85').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_26616></div>
                        <div id=showcode_85><br>196832998539485829<br>  </div>
                        <div id=info_85 style="font-size:7pt;">
					<a href=/admin/auth/user/385>user</a> | 
					<a href=/admin/contact/contact/26616>contact</a> | 
					<a href=/admin/reseller/reseller/85>reseller</a> | 
					<a href=/admin/auth/user/385/password>password</a> | 
			</div>

                        <div id=addcat_85>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=85">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=85">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=85">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=85">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=85">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=85">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=85">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_85').toggle();
				$('#addcat_85').toggle();
				$('#info_85').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/32173>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_32173').load('/show_affiliate?cid=32173');"><b><font color=#66023C>Travler&#39;s Choice</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=103 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=6947422276701503471 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_103').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>

			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/103">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_103').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_103').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_32173></div>
                        <div id=showcode_103><br>6947422276701503471<br>  </div>

                        <div id=info_103 style="font-size:7pt;">
					<a href=/admin/auth/user/465>user</a> | 
					<a href=/admin/contact/contact/32173>contact</a> | 
					<a href=/admin/reseller/reseller/103>reseller</a> | 
					<a href=/admin/auth/user/465/password>password</a> | 
			</div>
                        <div id=addcat_103>

                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=103">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=103">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=103">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=103">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=103">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=103">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=103">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_103').toggle();
				$('#addcat_103').toggle();
				$('#info_103').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/18657>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_18657').load('/show_affiliate?cid=18657');"><b><font color=#66023C>Trusted Tours &amp; Attractions</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=62 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=4986610978160837307 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_62').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>30 / 0</font>
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/62">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_62').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_62').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_18657></div>
                        <div id=showcode_62><br>4986610978160837307<br>  </div>
                        <div id=info_62 style="font-size:7pt;">
					<a href=/admin/auth/user/254>user</a> | 
					<a href=/admin/contact/contact/18657>contact</a> | 
					<a href=/admin/reseller/reseller/62>reseller</a> | 
					<a href=/admin/auth/user/254/password>password</a> | 
			</div>

                        <div id=addcat_62>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=62">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=62">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=62">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=62">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=62">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=62">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=62">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_62').toggle();
				$('#addcat_62').toggle();
				$('#info_62').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/30273>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_30273').load('/show_affiliate?cid=30273');"><b><font color=#66023C>University Of South Alabama</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=102 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-2194165454200066798 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_102').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        15 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/102">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_102').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_102').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_30273></div>
                        <div id=showcode_102><br>-2194165454200066798<br>  </div>
                        <div id=info_102 style="font-size:7pt;">
					<a href=/admin/auth/user/434>user</a> | 
					<a href=/admin/contact/contact/30273>contact</a> | 
					<a href=/admin/reseller/reseller/102>reseller</a> | 
					<a href=/admin/auth/user/434/password>password</a> | 
			</div>

                        <div id=addcat_102>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=102">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=102">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=102">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=102">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=102">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=102">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=102">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_102').toggle();
				$('#addcat_102').toggle();
				$('#info_102').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/29732>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_29732').load('/show_affiliate?cid=29732');"><b><font color=#66023C>Valerie Wilson Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=97 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=7334129826970277255 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_97').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        28.3 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/97">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_97').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_97').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_29732></div>
                        <div id=showcode_97><br>7334129826970277255<br>  </div>
                        <div id=info_97 style="font-size:7pt;">
					<a href=/admin/auth/user/431>user</a> | 
					<a href=/admin/contact/contact/29732>contact</a> | 
					<a href=/admin/reseller/reseller/97>reseller</a> | 
					<a href=/admin/auth/user/431/password>password</a> | 
			</div>

                        <div id=addcat_97>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=97">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=97">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=97">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=97">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=97">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=97">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=97">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_97').toggle();
				$('#addcat_97').toggle();
				$('#info_97').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
            <tr>  
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#abb3fb;height=100%">

<!--a class=mytd2 href=/admin/contact/contact/38>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_38').load('/show_affiliate?cid=38');"><b><font color=#66023C>Viator - All Tours</font></b></a><br>
                        &nbsp;&nbsp;<a href=/showReseller?rid=13 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=2178948234643887604 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_13').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                         
                           <font color=red>30 / 0</font>

                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/13">[edit]</a>
			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_13').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_13').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_38></div>
                        <div id=showcode_13><br>2178948234643887604<br>  </div>

                        <div id=info_13 style="font-size:7pt;">
					<a href=/admin/auth/user/18>user</a> | 
					<a href=/admin/contact/contact/38>contact</a> | 
					<a href=/admin/reseller/reseller/13>reseller</a> | 
					<a href=/admin/auth/user/18/password>password</a> | 
			</div>
                        <div id=addcat_13>

                           <br>Select category: <font style="font-size:6pt;">(Currently: CC Reseller)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=13">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=13">Couponing</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=13">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=13">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=13">Pow Wow</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;

                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=13">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=13">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_13').toggle();
				$('#addcat_13').toggle();
				$('#info_13').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/9793>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_9793').load('/show_affiliate?cid=9793');"><b><font color=#66023C>Wd World Travel</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=57 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=-5818818755233190668 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_57').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        0 / 23.8
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/57">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_57').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_57').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_9793></div>
                        <div id=showcode_57><br>-5818818755233190668<br>  </div>
                        <div id=info_57 style="font-size:7pt;">
					<a href=/admin/auth/user/174>user</a> | 
					<a href=/admin/contact/contact/9793>contact</a> | 
					<a href=/admin/reseller/reseller/57>reseller</a> | 
					<a href=/admin/auth/user/174/password>password</a> | 
			</div>

                        <div id=addcat_57>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=57">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=57">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=57">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=57">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=57">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=57">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=57">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_57').toggle();
				$('#addcat_57').toggle();
				$('#info_57').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
		
		
               <td NOWRAP style="vertical-align:top;">
                  <table width=100% ><tr>
                     <td NOWRAP>
                        
                        <div style="width:100%;background-color:#c1eae8;height=100%">
<!--a class=mytd2 href=/admin/contact/contact/14263>_</a-->
                        <a class=mytd2 href=# onclick="$('#showaff_14263').load('/show_affiliate?cid=14263');"><b><font color=#66023C>Worldpass Travel Group</font></b></a><br>

                        &nbsp;&nbsp;<a href=/showReseller?rid=50 style="font-size:10pt;">[Run Report]</a>
                        <a style="font-size:10pt;" href=http://securebookingshuttletours.com/?CODE=1302047290032131950 >[book]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#info_50').toggle();">[info]</a>
                        <br>&nbsp;&nbsp;&nbsp;&nbsp;
                        23.8 / 0
                        
                        <div align=right>
			  <a style="font-face:Verdana;font-size:7pt;" href="/admin/contact/reseller/50">[edit]</a>

			  <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#showcode_50').toggle();">[showcode]</a>
                          <a style="font-face:Verdana;font-size:7pt;" href="javascript:void(0);" onclick="$('#addcat_50').toggle();">[add to category]</a>
                        </div>
                        <div id=showaff_14263></div>
                        <div id=showcode_50><br>1302047290032131950<br>  </div>
                        <div id=info_50 style="font-size:7pt;">
					<a href=/admin/auth/user/214>user</a> | 
					<a href=/admin/contact/contact/14263>contact</a> | 
					<a href=/admin/reseller/reseller/50>reseller</a> | 
					<a href=/admin/auth/user/214/password>password</a> | 
			</div>

                        <div id=addcat_50>
                           <br>Select category: <font style="font-size:6pt;">(Currently: None)</font><br>
                           <div style=margin-left:10px;">
                                 <table><tr><td>(Unset)</td><td>&nbsp;&nbsp;<a href="/affiliates?cat=NOCAT&rid=50">(No category)</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f6b490;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f6b490&nbsp;&nbsp;<a href="/affiliates?cat=Couponing&rid=50">Couponing</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#abb3fb;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#abb3fb&nbsp;&nbsp;<a href="/affiliates?cat=CC Reseller&rid=50">CC Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#78e89a;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#78e89a&nbsp;&nbsp;<a href="/affiliates?cat=Reg Reseller&rid=50">Reg Reseller</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#f4b3c5;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#f4b3c5&nbsp;&nbsp;<a href="/affiliates?cat=Pow Wow&rid=50">Pow Wow</a></td></tr></table>

                              
                                 <table><tr><td><div style="background-color:#e7f981;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#e7f981&nbsp;&nbsp;<a href="/affiliates?cat=Travel Agent&rid=50">Travel Agent</a></td></tr></table>
                              
                                 <table><tr><td><div style="background-color:#d7d1d1;width:25px;">&nbsp;&nbsp;&nbsp;
                                 </div></td><td>#d7d1d1&nbsp;&nbsp;<a href="/affiliates?cat=Admin&rid=50">Admin</a></td></tr></table>
                              
                           </div>
                        </div>
                        <script>
				$('#showcode_50').toggle();
				$('#addcat_50').toggle();
				$('#info_50').toggle();
			</script>

&nbsp;&nbsp;&nbsp;&nbsp;</div>
                     </td></tr>
                  </table>
               </td>
	    
	    
            
            </tr>
         
      </table>
      <br>       
         <hr><div align=left><h3>Add reseller from user</h3></div>
         <table width=100%><tr>

            <td style="vertical-align:top;"><b>Special Reseller:  (Bypasses Credit Card Processing)</b><br>
                  <form action="." method=GET>
                     <input type=hidden name=addSpecial value=1>
                     <input type=hidden name=discount value=100>
                     <input type=hidden name=commission value=-100>
                        <table>
                           <tr>  <td>contact</td>

                                 <td>
                                       <select name=cid>
                                       
                                 </td></tr>
                           <tr><td>commission</td>    <td><input type=text name=commission style="width:30px">%</td></tr>
                           <tr><td>discount</td>      <td><input type=text name=discount2 style="width:30px">%</td></tr>
                           <tr><td></td>              <td><br><input type=submit value="add special"></td></tr>

                        </table>
                  </form>
            </td>
            <td style="vertical-align:top;"><b>Regular reseller</b><br>
               
                  <form action="." method=GET>
                     <input type=hidden name=add value=1>
                        <table>
                           <tr>  <td>contact</td>

                                 <td>
                                       <select name=cid>
                                       
                                 </td></tr>
                           <tr><td>commission</td>    <td><input type=text name=commission style="width:30px">%</td></tr>
                           <tr><td>discount</td>      <td><input type=text name=discount style="width:30px">%</td></tr>
                           <tr><td></td>              <td><br><input type=submit value="add reseller"></td></tr>

                        </table>
                  </form>
               
            </td></tr>
         </table>
   
</td></tr></table>
"""