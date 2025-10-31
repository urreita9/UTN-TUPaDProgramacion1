import itertools
import re

class ClasificadorLogico:
    def __init__(self):
        self.variables = set()
        self.operadores = {
            '¬': self.negacion,
            '~': self.negacion,
            '!': self.negacion,
            '∧': self.conjuncion,
            '&': self.conjuncion,
            '∨': self.disyuncion,
            '|': self.disyuncion,
            '⇒': self.implicacion,
            '→': self.implicacion,
            '>': self.implicacion,
            '⇔': self.bicondicional,
            '↔': self.bicondicional,
            '<>': self.bicondicional
        }
    
    def negacion(self, p):
        return not p
    
    def conjuncion(self, p, q):
        return p and q
    
    def disyuncion(self, p, q):
        return p or q
    
    def implicacion(self, p, q):
        return not p or q
    
    def bicondicional(self, p, q):
        return p == q
    
    def extraer_variables(self, expresion):
        """Extrae las variables proposicionales de la expresión"""
        # Buscar letras minúsculas que no sean operadores
        variables = re.findall(r'[a-z]', expresion.lower())
        self.variables = set(variables)
        return sorted(self.variables)
    
    def normalizar_expresion(self, expresion):
        """Normaliza la expresión reemplazando símbolos alternativos"""
        # Reemplazar operadores alternativos por símbolos estándar
        expresion = expresion.replace('~', '¬')
        expresion = expresion.replace('!', '¬')
        expresion = expresion.replace('&', '∧')
        expresion = expresion.replace('|', '∨')
        expresion = expresion.replace('->', '⇒')
        expresion = expresion.replace('=>', '⇒')
        expresion = expresion.replace('>', '⇒')
        expresion = expresion.replace('<->', '⇔')
        expresion = expresion.replace('<=>', '⇔')
        expresion = expresion.replace('<>', '⇔')
        return expresion
    
    def evaluar_expresion(self, expresion, valores):
        """Evalúa la expresión lógica con los valores dados"""
        # Reemplazar variables por sus valores
        expr_evaluada = expresion
        for var in self.variables:
            expr_evaluada = expr_evaluada.replace(var, str(valores[var]))
        
        # Evaluar expresión paso a paso
        return self.evaluar_recursivo(expr_evaluada)
    
    def evaluar_recursivo(self, expresion):
        """Evalúa la expresión de forma recursiva"""
        expresion = expresion.strip()
        
        # Caso base: True o False
        if expresion == 'True':
            return True
        if expresion == 'False':
            return False
        
        # Manejar paréntesis
        if expresion.startswith('(') and expresion.endswith(')'):
            return self.evaluar_recursivo(expresion[1:-1])
        
        # Buscar operadores en orden de precedencia (menor a mayor)
        # 1. Bicondicional (menor precedencia)
        for op in ['⇔']:
            if op in expresion:
                partes = self.dividir_por_operador(expresion, op)
                if len(partes) == 2:
                    izq = self.evaluar_recursivo(partes[0])
                    der = self.evaluar_recursivo(partes[1])
                    return self.bicondicional(izq, der)
        
        # 2. Implicación
        for op in ['⇒']:
            if op in expresion:
                partes = self.dividir_por_operador(expresion, op)
                if len(partes) == 2:
                    izq = self.evaluar_recursivo(partes[0])
                    der = self.evaluar_recursivo(partes[1])
                    return self.implicacion(izq, der)
        
        # 3. Disyunción
        for op in ['∨']:
            if op in expresion:
                partes = self.dividir_por_operador(expresion, op)
                if len(partes) == 2:
                    izq = self.evaluar_recursivo(partes[0])
                    der = self.evaluar_recursivo(partes[1])
                    return self.disyuncion(izq, der)
        
        # 4. Conjunción
        for op in ['∧']:
            if op in expresion:
                partes = self.dividir_por_operador(expresion, op)
                if len(partes) == 2:
                    izq = self.evaluar_recursivo(partes[0])
                    der = self.evaluar_recursivo(partes[1])
                    return self.conjuncion(izq, der)
        
        # 5. Negación (mayor precedencia)
        if expresion.startswith('¬'):
            return self.negacion(self.evaluar_recursivo(expresion[1:]))
        
        # Si llegamos aquí, debe ser una variable simple
        return expresion == 'True'
    
    def dividir_por_operador(self, expresion, operador):
        """Divide la expresión por el operador principal"""
        nivel_parentesis = 0
        for i, char in enumerate(expresion):
            if char == '(':
                nivel_parentesis += 1
            elif char == ')':
                nivel_parentesis -= 1
            elif char == operador[0] and nivel_parentesis == 0:
                if expresion[i:i+len(operador)] == operador:
                    return [expresion[:i].strip(), expresion[i+len(operador):].strip()]
        return [expresion]
    
    def generar_tabla_verdad(self, expresion):
        """Genera la tabla de verdad completa"""
        expresion = self.normalizar_expresion(expresion)
        variables = self.extraer_variables(expresion)
        
        if not variables:
            print("No se encontraron variables en la expresión.")
            return None
        
        # Generar todas las combinaciones posibles
        combinaciones = list(itertools.product([False, True], repeat=len(variables)))
        
        tabla = []
        resultados = []
        
        for combinacion in combinaciones:
            valores = dict(zip(variables, combinacion))
            
            # Convertir valores booleanos a string para evaluación
            valores_str = {}
            for var, val in valores.items():
                valores_str[var] = 'True' if val else 'False'
            
            try:
                resultado = self.evaluar_expresion(expresion, valores_str)
                tabla.append((*combinacion, resultado))
                resultados.append(resultado)
            except Exception as e:
                print(f"Error evaluando la expresión: {e}")
                return None
        
        return variables, tabla, resultados
    
    def clasificar_proposicion(self, resultados):
        """Clasifica la proposición según sus resultados"""
        if all(resultados):
            return "TAUTOLOGÍA", "La proposición es siempre verdadera"
        elif not any(resultados):
            return "CONTRADICCIÓN", "La proposición es siempre falsa"
        else:
            return "CONTINGENCIA", "La proposición puede ser verdadera o falsa"
    
    def mostrar_tabla(self, variables, tabla):
        """Muestra la tabla de verdad formateada"""
        # Encabezados
        header = " | ".join(variables) + " | Resultado"
        print("+" + "-" * len(header) + "+")
        print("|" + header + "|")
        print("+" + "-" * len(header) + "+")
        
        # Filas de datos
        for fila in tabla:
            valores_str = []
            for i, val in enumerate(fila[:-1]):
                valores_str.append("V" if val else "F")
            resultado_str = "V" if fila[-1] else "F"
            
            fila_str = " | ".join(valores_str) + " |    " + resultado_str
            print("|" + fila_str + "    |")
        
        print("+" + "-" * len(header) + "+")

def main():
    clasificador = ClasificadorLogico()
    
    print("=== CLASIFICADOR DE PROPOSICIONES COMPUESTAS ===")
    print("\nOperadores soportados:")
    print("  Negación: ¬, ~, !")
    print("  Conjunción (Y): ∧, &")
    print("  Disyunción (O): ∨, |")
    print("  Implicación: ⇒, ->, =>, >")
    print("  Bicondicional: ⇔, <->, <=>, <>")
    print("\nEjemplos de expresiones:")
    print("  - p∨¬p (tautología)")
    print("  - p∧¬p (contradicción)")
    print("  - p⇒q (contingencia)")
    print("  - (p∧q)⇒p (tautología)")
    
    while True:
        print("\n" + "="*50)
        expresion = input("\nIngrese una proposición compuesta (o 'salir' para terminar): ")
        
        if expresion.lower() == 'salir':
            break
        
        if not expresion.strip():
            continue
        
        # Generar tabla de verdad
        resultado = clasificador.generar_tabla_verdad(expresion)
        
        if resultado:
            variables, tabla, resultados = resultado
            
            print(f"\nExpresión analizada: {clasificador.normalizar_expresion(expresion)}")
            print(f"Variables encontradas: {', '.join(variables)}")
            print("\nTabla de Verdad:")
            
            clasificador.mostrar_tabla(variables, tabla)
            
            # Clasificar
            tipo, descripcion = clasificador.clasificar_proposicion(resultados)
            print(f"\n🔍 CLASIFICACIÓN: {tipo}")
            print(f"📝 Explicación: {descripcion}")
            
            # Estadísticas adicionales
            verdaderos = sum(resultados)
            total = len(resultados)
            print(f"📊 Estadísticas: {verdaderos}/{total} combinaciones verdaderas ({verdaderos/total*100:.1f}%)")

if __name__ == "__main__":
    main()