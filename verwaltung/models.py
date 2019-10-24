from django.db import models

# Create your models here.
class Klasse(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Klassen"


class Schueler(models.Model):
    vname = models.CharField(max_length=30, verbose_name='Vorname')
    nname = models.CharField(max_length=30, verbose_name='Nachname')
    email = models.EmailField()
    klasse = models.ForeignKey(Klasse, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)

    def __str__(self):
        if self.klasse is None:
            return '{} {}'.format(self.vname, self.nname)
        return '{} {}, {}'.format(self.vname, self.nname, self.klasse)

    def name(self):
        return self.vname + " " + self.nname

    class Meta:
        verbose_name = "Schüler"
        verbose_name_plural = "Schüler"


class Lehrer(models.Model):
    titel = models.CharField(max_length=10, verbose_name='Titel', blank=True, null=True, default=None)
    vname = models.CharField(max_length=30, verbose_name='Vorname')
    nname = models.CharField(max_length=30, verbose_name='Nachname')
    email = models.EmailField(verbose_name='Email')
    kuerzel = models.CharField(max_length=10, verbose_name='Kürzel')

    def __str__(self):
        if self.titel and self.titel != "":
            return "{} {} {}".format(self.titel, self.vname, self.nname)
        else:
            return "{} {}".format(self.vname, self.nname)


    class Meta:
        verbose_name = "Lehrer"
        verbose_name_plural = "Lehrer"


class Fach(models.Model):
    name = models.CharField(max_length=20)
    kuerzel = models.CharField(max_length=10, verbose_name='Kürzel')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fach"
        verbose_name_plural = "Fächer"


class Ergebnis(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ergebnis"
        verbose_name_plural = "Ergebnisse"


class Aktivitaet(models.Model):
    name = models.CharField(max_length=100)
    fach = models.ForeignKey(Fach, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aktivität"
        verbose_name_plural = "Aktivitäten"


class AktivitaetErgebnis(models.Model):
    aktivitaet = models.ForeignKey(Aktivitaet, on_delete=models.CASCADE, verbose_name='Aktivität')
    ergebnis = models.ForeignKey(Ergebnis, on_delete=models.CASCADE)
    mint_punkte = models.IntegerField(verbose_name='MINT-EC-Punkte')

    def __str__(self):
        return '{}: {}'.format(self.aktivitaet, self.ergebnis)

    class Meta:
        verbose_name = "Aktivitätsergebnis"
        verbose_name_plural = "Aktivitätsergebnisse"


class Schuljahr(models.Model):
    schuljahr =models.CharField(max_length=7, verbose_name='Schuljahr')

    def __str__(self):
        return self.schuljahr

    class Meta:
        verbose_name="Schuljahr"
        verbose_name_plural = "Schuljahre"



class Teilnahme(models.Model):
    schueler = models.ForeignKey(Schueler, on_delete=models.CASCADE, verbose_name="Schüler", related_name='teilnahmen')
    aktivitaetergebnis = models.ForeignKey(AktivitaetErgebnis, on_delete=models.PROTECT, verbose_name="Aktivitätsergebnis")
    lehrer1 = models.ForeignKey(Lehrer, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="1. Betreuender Lehrer", related_name='lehrer1_set')
    lehrer2 = models.ForeignKey(Lehrer, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="2. Betreuender Lehrer", related_name='lehrer2_set')
    schuljahr = models.ForeignKey(Schuljahr, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return '{}: {}'.format(self.schueler.name(), self.aktivitaetergebnis)

    class Meta:
        verbose_name = "Teilnahme"
        verbose_name_plural = "Teilnahmen"
