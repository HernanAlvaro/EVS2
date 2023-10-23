from django.shortcuts import render

# Create your views here.

def jujutsu_k(request):
    return render(request,'templates2/jujutsu.html')

def shibuya(request):
    data={
        "titulo":"Shibuya Arc",
        'Sinopsis arco':"A las 7:00 PM del 31 de octubre de 2018, aparece una extraña pantalla en la Prefectura de Shibuya que permite que los chamanes entren pero no salgan. Los habitantes encerrados dentro de la pantalla, piden por la aparición de Satoru Gojo, ya que su aparición es la única condición que necesitan para salir.",
        'imagen1':'/static/imagenesJujutsu/shibuya.jpg',
        
    }
    return render(request,'templates/templates2/jujutsu.html',data)

def ejecution(request):
    data={
        "titulo":"Ejecution Arc",
        'Sinopsis arco':"Tras los eventos ocurridos durante el Arco de El Incidente de Shibuya, el Departamento de Supervisión General de Jujutsu ha emitido un comunicado para castigar a los responsables de los sucedido. Dicho comunicado alega que: ① Se ha emitido una una nueva sentencia de muerte para Suguru Geto, ② Satoru Gojo es señalado como cómplice de lo sucedido, ③ Masamichi Yaga enfrentará la pena capital por incentivar a sus antiguos estudiantes, y ④ la ejecución de Yuji Itadori debe ser llevada a cabo inmediatamente por Yuta Okkotsu.",
        'imagen1':'/static/imagenesJujutsu/Ejecution Arc.jpg',
    }
    return render(request,'templates/templates2/jujutsu.html',data)

def preparation(request):
    data={
        "titulo":"Preparation Arc",
        'Sinopsis arco':"Tras haberse fingido nuevamente la muerte de Yuji Itadori, Megumi Fushiguro comunica que aquel que se hace llamar Noritoshi Kamo ha planeado una pelea, entre todos aquellos a los que otorgó la habilidad de utilizar técnicas y energía maldita, llamada Viaje a la Extinción, y en la cual, su hermana mayor, Tsumiki Fushiguro, también se ha visto envuelta. Para evitar que las cosas resulten a favor del enemigo, Megumi e Itadori intentan reunir al resto de compañeros para luchar juntos.",
        'imagen1':'/static/imagenesJujutsu/Preparation Arc.jpg',
    }
    return render(request,'templates/templates2/jujutsu.html',data)

