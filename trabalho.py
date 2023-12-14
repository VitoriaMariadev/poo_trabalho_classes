class Veiculo:
    def __init__(self, velocidade_maxima, km_rodados, marcha_automatico):
        self.velocidade_maxima = float(velocidade_maxima)
        self.km_rodados = float(km_rodados)
        self.marcha_automatico = bool(marcha_automatico)

    def __str__(self):
        return f"Velocidade Máxima: {self.velocidade_maxima} km/h, Quilômetros Rodados: {self.km_rodados} km, Marcha Automático: {self.marcha_automatico}"
    
class Onibus(Veiculo):
    def __init__(self, velocidade_maxima, km_rodados, marcha_automatico, numero_assentos):
        Veiculo.__init__(self, velocidade_maxima, km_rodados, marcha_automatico)
        self.numero_assentos = int(numero_assentos)

    def tarifa(self):
        return 5.0

    def __str__(self):
        return f"Velocidade Máxima: {self.velocidade_maxima} km/h, Quilômetros Rodados: {self.km_rodados} km, Marcha Automático: {self.marcha_automatico}, Número de Assentos: {self.numero_assentos}"

class MicroOnibus(Onibus):
    def tarifa(self):
        return 4.5

    
veiculo_objeto = Veiculo(velocidade_maxima=120.0, km_rodados=5000.0, marcha_automatico=True)

onibus_objeto = Onibus(velocidade_maxima=80.0, km_rodados=15000.0, marcha_automatico=True, numero_assentos=40)

print("Veículo Genérico:")
print(veiculo_objeto)

print("\nÔnibus de Exemplo:")
print(onibus_objeto)

onibus = Onibus(velocidade_maxima=80.0, km_rodados=15000.0, marcha_automatico=True, numero_assentos=40)
micro_onibus = MicroOnibus(velocidade_maxima=70.0, km_rodados=10000.0, marcha_automatico=True, numero_assentos=25)

print(f"Tarifa do Ônibus: R${onibus.tarifa()}")
print(f"Tarifa do MicroÔnibus: R${micro_onibus.tarifa()}")

class EmpresaOnibus:
    @staticmethod
    def faturamento(veiculo):
        if isinstance(veiculo, Onibus):
            return veiculo.tarifa() * onibus.numero_assentos

        else:
            return 0

print(f"Faturamento do ônibus: R${EmpresaOnibus.faturamento(onibus)}")
