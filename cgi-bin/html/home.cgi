#!/usr/bin/perl

print "Content-type: text/html\n\n";

print <<FINE;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title xml:lang="en" lang="en">Home Page - SitesBoard</title> 

		<link href="../../public_html/css/screen.css" rel="stylesheet" type="text/css" media="screen and (min-width:800px)"/>
		<link href="../../public_html/css/handheld.css" rel="stylesheet" type="text/css" media="handheld,screen and (max-width:800px)" />
		<link href="../../public_html/css/print.css" rel="stylesheet" type="text/css" media="print"/>
		


		<!-- Meta Tag-->
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
		<meta name="title" content="Home Page - SitesBoard" />
		<meta name="author" content="Davide Rigoni, Francesco Fasolato, Giacomo Zecchin, Antonino Macrì" />
		<meta name="description" content="Home Page di SitesBoard per la richiesta di Siti Web Professionali" />
		<meta name="keywords" content="Home, Bacheca, Siti, Web" />
		<meta name="language" content="italian it" />
		
		<script type="text/javascript" src="../../public_html/javascript/control.js"></script>
	</head>
	<body>
		<div id="container">



			<!-- HEADER-->
			<div id="header">
				<img id="header_logo" src="../media/logo.png" alt="Logo del sito SitesBoard" title = "Logo del sito"/>
				<h1>SitesBoard</h1>
				<h2>La <span xml:lang="en" lang="en">Sites Board</span> per richiedere Siti <span xml:lang="en" lang="en">Web</span></h2>

				<!-- Da caricare nel caso l'utente sia loggato -->
				<div id="header_login">
					<div>
						Benvenuto <span class="notable">Nome Cognome</span>
					</div>
					<div class="minimal">
						<!-- <a href="../administration/html/profile_change.html" hreflang="it" >Modifica Profilo<img id="header_PEL" src="../media/profile_edit.png" alt="Iconcina di modifica profilo" title = "Modifica i dati del profilo"/></a>-->
						<a href="../administration/html/profile_change.html" hreflang="it" >Modifica Profilo</a>
						o <a href="" hreflang="it" >Esci</a>
					</div>
				</div>
			</div>



			<!-- PATH -->
			<div id="path" title="Sezione del sito in cui ti trovi in questo momento">
				Ti trovi in: <span class="notable" xml:lang="en" lang="en">Home</span>
			</div>



			<div id="nav_panel">

				<!-- MENÙ DI NAVIGAZIONE -->
				<div id="nav_menu" class="menu" title ="Menù di navigazione del sito">
					<h3>Menù</h3>
					<p>Tipologia Siti:</p>
					<ul>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">E-commerce</span></a></li>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">Forum</span></a></li>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">Social</span></a></li>
						<li><a href="" hreflang="it" >Personali</a></li>
						<li><a href="" hreflang="it" >Aziendali</a></li>
						<li><a href="" hreflang="it" ><span xml:lang="en" lang="en">Blog</span></a></li>
					</ul>
					
				</div>



				<!-- MENÙ DI LOGIN-->
				<!-- Da caricare solo se l'utente non è loggato-->
				<div id="nav_login" class="menu" title="Menù di Login del sito">
					<h3><span xml:lang="en" lang="en">Login</span></h3>
					<!-- Messaggio di errore -->
					<p id="logErr" title="Messaggio di errore compilazione form login">
						<span xml:lang="en" lang="en">Password</span> e <span xml:lang="en" lang="en">Username</span> errati
					</p>
					<!-- Form da compilare -->
					<form onsubmit="return loginControl()" method="post" action="login.html">
						<fieldset title="Campi da compilare per effettuare il Login">
							<legend>Campi da compilare per effettuare il Login</legend>
							<label for="login_user">Username</label>
							<input type="text" name="login_user" id="login_user"/><br/>
							<label for="login_password">Password</label>
							<input type="password" name="login_password" id="login_password"/><br/>
						</fieldset>
						<fieldset title="Procedi su Login per effetturare l'accesso">
							<legend>Operazione di Login</legend>
							<input type="submit" name="login_submit" id="login_submit" value="Accedi al sito" />
						</fieldset>
					</form>
					<a class ="minimal" href="registration.html" hreflang="it" >Non ti sei ancora registrato?</a>
					<a class = "minimal" href="pass_recovery.html" hreflang="it" >Non trovi più la <span xml:lang="en" lang="en">password?</span></a>
				</div>


				<!-- Da caricare se l'utente è loggato-->
				<div id="nav_administration" class="menu" title="Menù di amministrazione del sito">
					<h3>Amministrazione</h3>
					<a href="" hreflang="it" >Esempio 1</a>
					<a href="" hreflang="it" >Esempio 2</a>
					<a href="" hreflang="it" >Esempio 3</a>
				</div>

			</div>




			<!-- CONTENUTI DELLA PAGINA -->
			<div id="contents">
				<h3><span xml:lang="en" lang="en">Home</span></h3>
				<div id="cont_welcome">Benvenuti nella sito SitesBoard. In questo sito potete vedere, proporre e anche accettare richieste di creazione di siti web.
				</div>
			</div>

			<!-- Div necessario per spostare il footer in fondo alla pagina -->
			<div id="push_block">
			</div>
		</div>




		<!-- FOOTER -->
		<div id="footer">
			<span title="Pagina validata con lo standard XHTML 1.0 Strict">
			    <a href="http://validator.w3.org/check?uri=referer" hreflang="en" >
			    	<img class="img_validator" src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" />
			    </a>
			</span>
			<span title="CSS della pagina validato secondo lo standard">
				<!--hrflang varia a seconda dello stato -->
			    <a href="http://jigsaw.w3.org/css-validator/check/referer" > 
			        <img class="img_validator" src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Valido!" />
			    </a>
			</span>
			<span title="Accessibile secondo lo standard WCAG2 Livello AAA">
			    <a href="http://www.w3.org/WAI/intro/wcag"  hreflang="en-US">
			        <img class="img_validator" src="https://www.totalvalidator.com/images/valid_n_wcag2_aaa.gif" alt="Pagina accessibile" />
			    </a>
			</span>
		</div>
	</body>
</html>

<!-- 
Aggiungere:
	- colori della pagina -> PROBLEMA
	
FINE
exit;