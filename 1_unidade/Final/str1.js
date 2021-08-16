var d1, n1, d2, n2, d3, n3, d4, n4;
media = 0;
pontos = 0;
acertou = false;
countBolas = 0;
fimDoJogo = false;
clicou = false;
podeApertar = false;
aparecerBola = false;
pegarTempo1 = false;
pegarTempoClique = false;
countMenu = 0;
fezSorteio = false;

function initialScreen() {
	textSize(32);
	fill(0,0,0);
	stroke(0,0,0);
	text("PRESSIONE ESPAÇO PARA INICIAR",220,250);
	textSize(10);
	text("UP",393,330);
	text("DOWN",434,330);
	text("LEFT",487,330);
	text("RIGHT",535,330);
	stroke(0,0,0);
	fill("blue");
	ellipse(400,300,30);
	fill("yellow");
	ellipse(450,300,30);
	fill("red");
	ellipse(500,300,30);
	fill("green");
	ellipse(550,300,30,30);
}

function endingScreen() {
	textSize(32);
	fill(0,0,0);
	text("MÉDIA: " + media.toFixed(2) +"ms", 150, 200);
	text("SCORE: " + pontos, 150, 240);
	text("PRESSIONE ENTER PARA CONTINUAR", 150, 280);
}

function sorteio() {
	var circle = {
		cor: Math.floor(Math.random() * 4) + 1, // Cores de 1 a 4. 1: azul, 2: amarelo, 3: vermelho, 4: verde
		tempo: Math.floor(Math.random() * 4) + 2, // Tempo de 2 a 5 segundos
		posicaoX: Math.floor(Math.random() * 900) + 50, // Coordenada x da bola de 50 a 950
		posicaoY: Math.floor(Math.random() * 350) + 75 // Coordenada y da bola de 75 a 425
	}
	return circle;
}

function showCircle(circle) {
	stroke(0,0,0);
	if (circle.cor == 1) {
		fill("blue");
		ellipse(circle.posicaoX, circle.posicaoY, 30);
	} else if (circle.cor == 2) {
		fill("yellow");
		ellipse(circle.posicaoX, circle.posicaoY, 30);
	} else if (circle.cor == 3) {
		fill("red");
		ellipse(circle.posicaoX, circle.posicaoY, 30);
	} else {
		fill("green");
		ellipse(circle.posicaoX, circle.posicaoY, 30);
	}
}

function setup() {
	createCanvas(1000, 512); 
	frameRate(60);
}

function draw() {
	background(200);
	fill(0,0,0);
	noStroke();
	if (keyIsDown(32)) {
		countMenu = 1;
	}
	if (countMenu == 0) {
		initialScreen();	
	} else if (fimDoJogo == true) {
		endingScreen();
		if(keyIsDown(13)){
			countMenu = 0;
			fimDoJogo = false;
			pontos = 0;
			countBolas = 0;
			clicou = false;
			pegarTempo1 = false;
			pegarTempoClique = false;
			podeApertar = false;
			media = false;
			fezSorteio = false;
			aparecerBola = false;
			acertou = false;
		}
		
	} else {
		textSize(32);
		fill(0,0,0);
		text("SCORE: " + pontos, 400, 32);
		if (fezSorteio == false) {
			circleShown = sorteio();
			fezSorteio = true;
		}
		if (pegarTempo1 == false) {
			d1 = new Date();
			n1 = d1.getTime();
			pegarTempo1 = true;
		}
		d2 = new Date();
		n2 = d2.getTime();
		if (n2 - n1 >= circleShown.tempo * 1000) {
			aparecerBola = true;
			pegarTempo1 = false;
		}
		if (aparecerBola == true) {
			if (pegarTempoClique == false) {
				d3 = new Date();
				n3 = d3.getTime();
				pegarTempoClique = true;
			}
			showCircle(circleShown);
			podeApertar = true;
		}
		if (podeApertar == true) {
			if (keyIsDown(38)) {
				clicou = true;
				if (circleShown.cor == 1) {
					pontos++;
					acertou = true;
				}
			} else if (keyIsDown(40)) {
				clicou = true;
				if (circleShown.cor == 2) {
					pontos++;
					acertou = true;
				}
			} else if (keyIsDown(37)) {
				clicou = true;
				if (circleShown.cor == 3) {
					pontos++;
					acertou = true;
				}
			} else if (keyIsDown(39)) {
				clicou = true;
				if (circleShown.cor == 4) {
					pontos++;
					acertou = true;
				}
			}
			if (clicou == true) {
				clicou = false;
				pegarTempoClique = false;
				countBolas++;
				aparecerBola = false;
				fezSorteio = false;
				podeApertar = false;
			}
			if (acertou == true) {
				d4 = new Date();
				n4 = d4.getTime();
				media += (n4 - n3);
				/*textSize(32);
				fill(255,255,255);
				text(n4 - n3, 10, 32);*/
				console.log(n4-n3);
				acertou = false;
			}
		}
		if (countBolas == 10) {
			fimDoJogo = true;
			if (pontos != 0) {
				media /= pontos;
			}
		}		
	}
	
	
	//informacoes();
	
	
	
}