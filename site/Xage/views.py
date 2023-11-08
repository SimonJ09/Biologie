from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import ContactForm

from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render, redirect

def service(request):
    return render(request, 'Xage/service.html')

def projet(request):
    return render(request, 'Xage/projet.html')

def about(request):
    return render(request, 'Xage/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # Récupérez les données du formulaire
            name = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            option = form.cleaned_data['option']

            # Construisez le contenu de l'e-mail
            subject = 'Nouveau message de {}'.format(name)
            body = 'Nom: {}\nEmail: {}\nMessage:\n{}'.format(name, email, message, option)

            # Configurer les détails du serveur SMTP
            smtp_server = 'smtp.gmail.com'  # Remplacez par le serveur SMTP de votre fournisseur de messagerie
            smtp_port = 587  # Port SMTP (587 est généralement utilisé pour TLS)
            smtp_username = 'judesimongbeliana@gmail.com'  # Votre adresse e-mail
            smtp_password = 'Simon09@09@09'  # Votre mot de passe

            # Créez un objet MIMEText pour l'e-mail
            msg = MIMEText(body)

            # Configurez les en-têtes de l'e-mail
            msg['Subject'] = subject
            msg['From'] = smtp_username
            msg['To'] = 'judesimongbeliana@gmail.com'  # Adresse e-mail de destination

            try:
                # Établissez une connexion SMTP sécurisée
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(smtp_username, smtp_password)

                # Envoyez l'e-mail
                server.sendmail(smtp_username, 'judesimongbeliana@gmail.com', msg.as_string())

                # Fermez la connexion SMTP
                server.quit()

                # Redirigez l'utilisateur vers une page de remerciement
                return redirect('merci')

            except Exception as e:
                # Gérez les erreurs d'envoi d'e-mail ici
                return render(request, 'erreur.html', {'error_message': str(e)})

    else:
        form = ContactForm()

    return render(request, 'Xage/contact.html', {'form': form})


#def articles(request):
    #return render(request, 'Xage/articles.html')

