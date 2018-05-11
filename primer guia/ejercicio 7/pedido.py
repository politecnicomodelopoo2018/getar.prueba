class Pedido(object):
    persona = None
    plato = None
    fecha_pedido = None
    hora_entrega = None
    entregado = None

    def __init__(self,fecha_pedido,UnaPersona,UnPlato,hora_entrega,entregado):
        self.persona = UnaPersona
        self.plato = UnPlato
        self.fecha_pedido = fecha_pedido
        self.hora_entrega = hora_entrega
        self.entregado = entregado

