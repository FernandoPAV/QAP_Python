# -*- coding: utf-8 -*-
"""QAP_solver.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FNIjef8nDyQGniLCeEGQN-UmjI_kh1Ib

## Gato
"""

cats = [
  "｡＾･ｪ･＾｡",
  "( ͒ ु- •̫̮ – ू ͒)",
  "( ^..^)ﾉ",
  "( =①ω①=)",
  "( =ω=)..nyaa",
  "( =ノωヽ=)",
  "(´; ω ;｀)",
  "(^-人-^)",
  "(^･o･^)ﾉ”",
  "(^・ω・^ )",
  "(^._.^)ﾉ",
  "(^人^)",
  "(・∀・)",
  "(,,◕　⋏　◕,,)",
  "(.=^・ェ・^=)",
  "(｡･ω･｡)",
  "((≡^⚲͜^≡))",
  "((ΦωΦ))",
  "(*^ω^*)",
  "(*✧×✧*)",
  "(*ΦωΦ*)",
  "(⁎˃ᆺ˂)",
  "(ٛ⁎꒪̕ॢ ˙̫ ꒪ٛ̕ॢ⁎)",
  "₍˄·͈༝·͈˄₎◞ ̑̑ෆ⃛",
  "₍˄·͈༝·͈˄₎ฅ˒˒",
  "₍˄ุ.͡˳̫.˄ุ₎ฅ˒˒",
  "(=｀ω´=)",
  "(=｀ェ´=)",
  "（=´∇｀=）",
  "(=^ ◡ ^=)",
  "(=^-ω-^=)",
  "(=^･^=)",
  "(=^･ω･^)y＝",
  "(=^･ω･^=)",
  "(=^･ｪ･^=)",
  "(=^‥^=)",
  "(=･ω･=)",
  "(=;ω;=)",
  "(=;ェ;=)",
  "(=；ェ；=)",
  "(=;ェ;=)",
  "(=；ェ；=)",
  "(=；ｪ；=)",
  "(=‘ｘ‘=)",
  "(=⌒‿‿⌒=)",
  "(=ↀωↀ=)",
  "(=ↀωↀ=)✧",
  "(=①ω①=)",
  "(=ＴェＴ=)",
  "(=ｘェｘ=)",
  "(=ΦｴΦ=)",
  "(ٛ₌டுͩ ˑ̭ டுͩٛ₌)ฅ",
  "(≚ᄌ≚)ℒℴѵℯ❤",
  "(≚ᄌ≚)ƶƵ",
  "(○｀ω´○)",
  "(●ↀωↀ●)",
  "(●ↀωↀ●)✧",
  "(✦థ ｪ థ)",
  "(ↀДↀ)",
  "(ↀДↀ)⁼³₌₃",
  "(ↀДↀ)✧",
  "(๑•ω•́ฅ✧",
  "(๑ↀᆺↀ๑)☄",
  "(๑ↀᆺↀ๑)✧",
  "(p`･ω･´) q",
  "(p`ω´) q",
  "(Φ∇Φ)",
  "(ΦεΦ)",
  "(ΦωΦ)",
  "(ΦёΦ)",
  "(ΦзΦ)",
  "(ฅ`･ω･´)っ=",
  "(ฅ`ω´ฅ)",
  "(ฅ’ω’ฅ)",
  "(ะ`♔´ะ)",
  "(ะ☫ω☫ะ)",
  "(ㅇㅅㅇ❀)",
  "(ノω<。)",
  "(ꀄꀾꀄ)",
  "（三ФÅФ三）",
  "[ΦωΦ]",
  "] ‘͇̂•̩̫’͇̂ ͒)ฅ ﾆｬ❣",
  "＼(=^‥^)/’`",
  "<(*ΦωΦ*)>",
  "<ΦωΦ>",
  "|ΦωΦ|",
  "|ｪ･`｡)･･･　　",
  "~(=^‥^)",
  "~(=^‥^)_旦~",
  "~(=^‥^)/",
  "~(=^‥^)ノ",
  "~□Pヘ(^･ω･^=)~",
  "⊱ฅ•ω•ฅ⊰",
  "└(=^‥^=)┐",
  "✩⃛( ͒ ु•·̫• ू ͒)",
  "❤(´ω｀*)",
  "ヽ(^‥^=ゞ)",
  "ヾ(*ΦωΦ)ﾉ",
  "ヾ(*ФωФ)βyё βyё☆彡",
  "ヾ(=｀ω´=)ノ”",
  "ヽ(=^･ω･^=)丿",
  "ヾ(=ﾟ･ﾟ=)ﾉ",
  "0( =^･_･^)=〇",
  "٩(ↀДↀ)۶",
  "b(=^‥^=)o",
  "d(=^･ω･^=)b",
  "o(^・x・^)o",
  "o(=・ω・=o)",
  "V(=^･ω･^=)v",
  "ლ(=ↀωↀ=)ლ",
  "ლ(●ↀωↀ●)ლ",
  "ฅ ̂⋒ิ ˑ̫ ⋒ิ ̂ฅ",
  "ฅ( ᵕ ω ᵕ )ฅ",
  "ฅ(´-ω-`)ฅ",
  "ฅ(´・ω・｀)ฅ",
  "ฅ(^ω^ฅ)",
  "ฅ(≚ᄌ≚)",
  "ฅ(⌯͒• ɪ •⌯͒)ฅ❣",
  "ฅ⃛(⌯͒꒪ั ˑ̫ ꒪ั ⌯͒) ﾆｬｯ❣",
  "ฅ(●´ω｀●)ฅ",
  "ฅ*•ω•*ฅ♡",
  "ฅ•ω•ฅ",
  "ฅ⊱*•ω•*⊰ฅ",
  "ㅇㅅㅇ",
  "ミ๏ｖ๏彡",
  "ミ◕ฺｖ◕ฺ彡",
  "=＾● ⋏ ●＾=",
  "ฅ^•ﻌ•^ฅ",
  "₍ᵔ·͈༝·͈ᵔ₎",
  "ฅ(⌯͒•̩̩̩́ ˑ̫ •̩̩̩̀⌯͒)ฅ",
  "₍˄·͈༝·͈˄*₎◞ ̑̑",
  "ଲ( ⓛ ω ⓛ *)ଲ",
  "=^._.^= ∫",
  "ଲ(⁃̗̀̂❍⃓ˑ̫❍⃓⁃̠́̂)ଲ"
]

"""# QAP

## QAP_Instance
"""

import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas
import random  # Importar el módulo random para generar números aleatorios
from copy import deepcopy  # Importar la función deepcopy para realizar copias de objetos
from enum import Enum  # Importar la clase Enum para definir enumeraciones
from itertools import combinations  # Importar la función combinations para generar combinaciones
from scipy.optimize import quadratic_assignment # Importar método faq desde SciPy

class QAP_Instance:
    def __init__(self, flujo, distancia):
        self.matriz_flujo = flujo  # Almacenar la matriz de flujo de la instancia del QAP
        self.matriz_distancia = distancia  # Almacenar la matriz de distancia de la instancia del QAP

"""## QAP_State"""

class QAP_State:
    def __init__(self, instance, matriz_asignacion=[0]):
        self.instance = instance  # Instancia del QAP
        self.matriz_asignacion = matriz_asignacion  # Asignación de localidades a instalaciones
        self.matriz_no_asignados = set(range(len(self.instance.matriz_flujo))) - set(self.matriz_asignacion)  # Localidades no asignadas
        self.todos_asignados = len(self.matriz_no_asignados) == 0  # ¿Todas las localidades están asignadas?
        self.costo = 0  # Costo del estado
        self.actualizar_costo()  # Actualizar el costo inicial del estado

    def calcular_costo(self, local1, local2):
      instalacion1 = self.matriz_asignacion[local1]
      instalacion2 = self.matriz_asignacion[local2]
      return self.instance.matriz_flujo[instalacion1][instalacion2] * \
            self.instance.matriz_distancia[local1][local2]

    def actualizar_costo(self):
        # Actualizar el costo total del estado sumando los costos de todas las asignaciones
        n = len(self.matriz_asignacion)
        if n > 1:
            costo = 0
            for i in range(n):
                for j in range(n):
                    costo += self.calcular_costo(i, j)
            self.costo = costo

    def __deepcopy__(self, memo):
        # Realizar una copia profunda del estado
        new_instance = type(self)(
            instance=deepcopy(self.instance, memo),
            matriz_asignacion=deepcopy(self.matriz_asignacion, memo)
        )
        return new_instance

    def __str__(self):
        # Representación en cadena del estado mostrando la asignación y el costo
        return f"Asignación : {self.matriz_asignacion}\nCosto      : {self.costo}"

"""## Move_Type"""

class MoveType(Enum):
  CONSTRUCTIVE = 1
  SWAP = 2
  TWO_OPT = 3
  RELOCATION = 4

"""## QAP_Environment"""

class QAP_Environment:
    @staticmethod
    def gen_actions(state, move_type, shuffle=False):
        # Genera acciones disponibles según el tipo de movimiento
        if move_type == MoveType.CONSTRUCTIVE:
            actions = [(move_type, instalacion) for instalacion in state.matriz_no_asignados]

        elif move_type == MoveType.SWAP:
            # Genera todas las combinaciones posibles de intercambio de instalaciones
            n = len(state.matriz_asignacion)
            actions = [(move_type, (i, j)) for i in range(n - 1) for j in range(i + 1, n)]

        elif move_type == MoveType.TWO_OPT:
            # Genera todas las combinaciones posibles de intercambio de instalaciones
            n = len(state.matriz_asignacion)
            actions = [(move_type, (i, j)) for i in range(n - 1) for j in range(i + 1, n)]

        elif move_type == MoveType.RELOCATION:
            # Genera todas las posibles reubicaciones de instalaciones
            n = len(state.matriz_asignacion)
            actions = [(move_type, (i, j)) for i in range(n) for j in range(n) if i != j]

        else:
            raise NotImplementedError(f"Tipo de acción '{move_type}' no implementado")

        # Opcionalmente, se mezclan las acciones para explorar de forma aleatoria
        if shuffle:
            random.shuffle(actions)

        # Generador que produce cada acción
        for action in actions:
            yield action

    @staticmethod
    def state_transition(state, action):
        # Realiza la transición de estado según la acción aplicada
        if action[0] == MoveType.CONSTRUCTIVE and not state.todos_asignados:
            # Agrega una instalación si no están todas asignadas
            state.matriz_asignacion.append(action[1])
            state.matriz_no_asignados.remove(action[1])
            if not state.matriz_no_asignados:
                state.actualizar_costo()
                state.todos_asignados = True
        elif action[0] == MoveType.SWAP and state.todos_asignados:
            # Intercambia dos instalaciones si todas están asignadas
            i, j = action[1]
            state.matriz_asignacion[i], state.matriz_asignacion[j] = state.matriz_asignacion[j], state.matriz_asignacion[i]
            state.actualizar_costo()
        elif action[0] == MoveType.TWO_OPT and state.todos_asignados:
            # Aplica la estrategia de intercambio 2-opt si todas están asignadas
            i, j = action[1]
            if i < j:
                i, j = j, i
            state.matriz_asignacion[i:j+1] = reversed(state.matriz_asignacion[i:j+1])
            state.actualizar_costo()
        elif action[0] == MoveType.RELOCATION and state.todos_asignados:
            # Reubica una instalación si todas están asignadas
            i, j = action[1]
            if i < j:
                state.matriz_asignacion.insert(j - 1, state.matriz_asignacion.pop(i))
            else:
                state.matriz_asignacion.insert(j, state.matriz_asignacion.pop(i))
            state.actualizar_costo()
        else:
            raise NotImplementedError(f"Movimiento '{action[0]}' no válido para estado {state}, all asigned: {state.todos_asignados}, not matriz_asignacion: {state.matriz_no_asignados}")
        return state

    @staticmethod
    def calcular_costo_after_action(state, action):
      if action[0] == MoveType.SWAP:
        k, l = action[1]

        state.matriz_asignacion[k], state.matriz_asignacion[l] = \
          state.matriz_asignacion[l], state.matriz_asignacion[k]

        new_costo = 0
        n = len(state.matriz_asignacion)
        for i in range(n):
          for j in range(n):
            instalacion1 = state.matriz_asignacion[i]
            instalacion2 = state.matriz_asignacion[j]
            local1 = i
            local2 = j
            new_costo += state.instance.matriz_flujo[instalacion1][instalacion2] * \
                        state.instance.matriz_distancia[local1][local2]

        state.matriz_asignacion[l], state.matriz_asignacion[k] = \
          state.matriz_asignacion[k], state.matriz_asignacion[l]

        return new_costo

      return state.costo

"""## Agente constructivo"""

def evalConstructiveActions(state, env):
    # Inicializa la lista de evaluaciones
    evals = []

    # Obtiene la última instalación asignada y el número total de instalaciones asignadas
    instalacion1 = state.matriz_asignacion[-1]
    n = len(state.matriz_asignacion)
    local1 = n - 1  # Índice de la última instalación asignada

    # Itera sobre la acción constructiva generada
    for action in env.gen_actions(state, MoveType.CONSTRUCTIVE):
        instalacion2 = action[1]

        # Salta la acción si la instalación actual ya está asignada
        if instalacion1 == instalacion2:
            continue

        # Calcula el costo asociado a la acción
        costo = -state.instance.matriz_flujo[instalacion1][instalacion2] * \
                state.instance.matriz_distancia[local1][local1]

        # Agrega la evaluación de la acción y su costo a la lista de evaluaciones
        evals.append((action, -costo))

    return evals

"""## Greedy"""

class GreedyAgent:
    def __init__(self, eval_actions):
        # Inicializa el agente con la función de evaluación de acciones
        self.eval_actions = eval_actions

    def reset(self):
        # Método para restablecer el estado del agente
        pass

    def select_action(self, evals):
        # Selecciona la acción con el mayor valor de evaluación
        return max(evals, key=lambda x: x[1])[0]

    def action_policy(self, state, env):
        # Obtiene las evaluaciones de las acciones para el estado dado
        evals = self.eval_actions(state, env)

        # Retorna None si no hay evaluaciones disponibles
        if not evals:
            return None

        # Retorna la acción con la mayor evaluación
        return self.select_action(evals)

    def __deepcopy__(self, memo):
        # Realiza una copia profunda del agente
        new_instance = type(self)(
            eval_actions=self.eval_actions,
        )
        return new_instance

"""## Local Search"""

class LocalSearchAgent(GreedyAgent):
    def __init__(self, move_type, first_improvement=True):
        # Inicializa el agente de búsqueda local con el tipo de acción y la opción de mejora inicial
        self.move_type = move_type
        self.first_improvement = first_improvement

    def eval_actions(self, state, env):
        # Evalúa las acciones posibles para mejorar el estado actual
        costo_actual = state.costo
        evals = []

        for action in env.gen_actions(state, self.move_type, shuffle=True):
            # Calcula el nuevo costo después de aplicar la acción
            nuevo_costo = env.calcular_costo_after_action(state, action)

            # Agrega la acción si mejora el costo actual
            if nuevo_costo < costo_actual:
                evals.append((action, nuevo_costo))
                if self.first_improvement:
                    return evals

        return evals

    def __deepcopy__(self, memo):
        # Realiza una copia profunda del agente de búsqueda local
        new_instance = type(self)(
            move_type=self.move_type,
            first_improvement=self.first_improvement
        )
        return new_instance

"""## Single Agent Solver"""

class SingleAgentSolver:
    def __init__(self, env, agent):
        # Inicializa el solver con un entorno y un agente
        self.env = env
        self.agent = agent

    def solve(self, state, track_best_state=False, save_history=False, max_actions=0):
        # Resuelve el problema con un solo estado inicial
        history = None

        if save_history:
            history = [(None, state.costo)]

        if max_actions == 0:
            max_actions = float('inf')

        best_state = None

        if track_best_state:
            best_state = deepcopy(state)

        self.agent.reset()

        n_actions = 0
        while n_actions < max_actions:
            # Selección de acción y transición de estado
            action = self.agent.action_policy(state, self.env)
            if action is None:
                break

            state = self.env.state_transition(state, action)
            n_actions += 1

            if track_best_state and state.costo < best_state.costo:
                best_state = deepcopy(state)

            if save_history:
                history.append((action, state.costo))

        if track_best_state:
            return best_state, history
        else:
            return state, history, n_actions

    def multistate_solve(self, states, track_best_state=False, save_history=False, max_actions=0):
        # Resuelve múltiples estados con un mismo agente
        agents = [deepcopy(self.agent) for _ in range(len(states))]
        history = [None] * len(states)
        best_state = [None] * len(states)
        n_actions = [None] * len(states)

        if max_actions == 0:
            max_actions = float('inf')

        for i in range(len(states)):
            agents[i].reset()
            n_actions[i] = 0
            history[i] = []
            if track_best_state:
                best_state[i] = deepcopy(states[i])

        live_states_idx = list(range(len(states)))

        for _ in range(max_actions):
            # Itera sobre los estados y selecciona las acciones óptimas
            evals = agents[0].eval_actions([states[i] for i in live_states_idx], self.env)

            new_idx = []
            for i in live_states_idx:
                eval = evals[live_states_idx.index(i)]

                if eval == []:
                    continue

                action = agents[i].select_action(eval)

                states[i] = self.env.state_transition(states[i], action)
                n_actions[i] += 1

                new_idx.append(i)

                if track_best_state and states[i].costo < best_state[i].costo:
                    best_state[i] = deepcopy(states[i])

                if save_history:
                    history[i].append((action, states[i].costo))

            live_states_idx = new_idx

            if not new_idx:
                break

        if track_best_state:
            return best_state, history
        else:
            return states, history, n_actions

"""## Perturbación"""

class Perturbation:
    def __init__(self, move_type, pert_size=10):
        # Inicializa la perturbación con el tipo de acción y el tamaño de perturbación
        self.pert_size = pert_size
        self.move_type = move_type

    def __call__(self, state, env):
        # Método para aplicar la perturbación al estado dado y devolver el estado perturbado
        gen_action = env.gen_actions(state, self.move_type, shuffle=True)
        # Genera acciones de manera aleatoria y las aplica al estado
        for _ in range(self.pert_size):
            action = next(gen_action)
            env.state_transition(state, action)
        return state

"""## Criterio de aceptación"""

def default_acceptance_criterion(min_costo, new_costo):
    return new_costo <= min_costo

"""## Iterated Local Search"""

class ILS_Solver:
    def __init__(self, constructive_solver, local_search_solver, perturbation,
                 acceptance_criterion=default_acceptance_criterion):
        # Inicializa el solucionador ILS con solucionadores constructivos y de búsqueda local,
        # una perturbación y un criterio de aceptación
        self.constructive_solver = constructive_solver
        self.local_search_solver = local_search_solver
        self.perturbation = perturbation
        self.acceptance_criterion = acceptance_criterion
        self.env = local_search_solver.env  # Establece el entorno del solucionador de búsqueda local

    def solve(self, initial_state, save_history=False, max_actions=0):
        # Método para resolver el problema usando Iterated Local Search (ILS)

        history = None  # Historial de acciones realizadas

        # Se resuelve el problema de manera constructiva y se aplica la búsqueda local
        current_solution, *_ = self.constructive_solver.solve(initial_state)
        current_solution, _history, n_act = self.local_search_solver.solve(current_solution, save_history=save_history)

        # Actualización del historial y el número de acciones
        if save_history:
            history = _history
        n_actions = n_act

        # Inicialización de la mejor solución
        best_solution = deepcopy(current_solution)

        # Bucle principal de Iterated Local Search
        while n_actions < max_actions:
            # Se aplica la perturbación a la solución actual
            perturbed_solution = self.perturbation(deepcopy(current_solution), self.env)
            perturbed_solution.actualizar_costo()  # Se actualiza el costo de la solución perturbada

            # Se aplica la búsqueda local a la solución perturbada
            local_optimum, hist, n_act = self.local_search_solver.solve(perturbed_solution, save_history=save_history, max_actions=max_actions-n_actions)

            # Actualización del historial y el número de acciones
            if save_history:
                history += hist
            n_actions += n_act

            costo = local_optimum.costo  # Se obtiene el costo de la solución local óptima encontrada

            # Se verifica si se acepta la nueva solución como la mejor solución actual
            if self.acceptance_criterion(best_solution.costo, costo):
                current_solution = local_optimum  # La solución actual se actualiza a la solución local óptima

                if costo < best_solution.costo:
                    best_solution = deepcopy(current_solution)  # Si la solución es la mejor hasta ahora, se actualiza la mejor solución

        return best_solution, history, n_actions  # Devuelve la mejor solución encontrada, el historial de acciones y el número total de acciones realizadas

"""## Tabu Search"""

class TabuSearchSolver:
    def __init__(self, move_type, tabu_size, budget):
        # Inicializa el solucionador de búsqueda tabú con el tipo de movimiento, el tamaño de la lista tabú y el presupuesto
        self.move_type = move_type
        self.tabu_size = tabu_size
        self.budget = budget
        self.tabu_list = []  # Lista tabú para almacenar acciones prohibidas

    def reset(self):
        # Reinicia el solucionador eliminando la lista tabú y restableciendo el iterador
        self.tabu_list.clear()
        self.iter = 0

    def solve(self, state, env):
        # Método para resolver el problema utilizando búsqueda tabú

        costo_actual = state.costo
        best_state = deepcopy(state)
        best_costo = costo_actual

        # Bucle principal de búsqueda tabú
        while self.iter < self.budget:
            # Selecciona una acción utilizando la política de acción
            action = self.action_policy(state, env)
            if action is None:
                break

            # Realiza la transición de estado según la acción seleccionada
            state = env.state_transition(state, action)
            new_costo = state.costo

            # Actualiza la mejor solución y su costo
            if new_costo < best_costo:
                best_state = deepcopy(state)
                best_costo = new_costo

            # Actualiza la lista tabú
            self.update_tabu_list(action)

    def action_policy(self, state, env):
        # Política para seleccionar una acción basada en el estado actual y el entorno

        if self.iter >= self.budget:
            return None

        best_costo = np.inf
        best_action = None

        # Itera sobre todas las acciones generadas por el entorno
        for action in env.gen_actions(state, self.move_type):
            if action in self.tabu_list:  # Se salta las acciones en la lista tabú
                continue

            # Calcula el costo después de aplicar la acción
            new_costo = env.calcular_costo_after_action(state, action)
            if new_costo < best_costo:  # Actualiza la mejor acción si mejora el costo
                best_costo = new_costo
                best_action = action

        # Trunca la lista tabú para mantener su tamaño
        self.tabu_list = self.tabu_list[-self.tabu_size:]

        self.iter += 1
        return best_action

    def select_action(self, evals):
        # Selecciona la acción con el mayor valor de evaluación
        return max(evals, key=lambda x: x[1])[0]

    def update_tabu_list(self, action):
        # Actualiza la lista tabú añadiendo la última acción y eliminando las acciones más antiguas si la lista excede el tamaño máximo
        self.tabu_list.append(action)
        if len(self.tabu_list) > self.tabu_size:
            self.tabu_list.pop(0)  # Elimina la acción más antigua

"""## Ejemplos individuales"""

# Flow entre instalaciones (facilities)
flow = np.array([[ 0,  8,  4,  1, 10],
       [ 8,  0,  7,  5, 10],
       [ 4,  7,  0,  3,  5],
       [ 1,  5,  3,  0,  4],
       [10, 10,  5,  4,  0]])

# Distancia entre ubicaciones (locations)
distance = np.array([[ 0,  8,  3,  5,  1],
       [ 8,  0,  6,  7,  4],
       [ 3,  6,  0,  5, 10],
       [ 5,  7,  5,  0,  1],
       [ 1,  4, 10,  1,  0]])

env = QAP_Environment
instance = QAP_Instance(flow, distance)

# Greedy
current_state = QAP_State(instance)
agent = GreedyAgent(evalConstructiveActions)

while True:

  action = agent.action_policy(current_state, env)
  if action is None:
    break

  current_state = env.state_transition(current_state, action)

print(f"Resultado Greedy:\n{current_state}\n")

# SLS
agent = LocalSearchAgent(MoveType.SWAP, first_improvement=True,)

# iteramos hasta llegar a un óptimo local
while True:

  action = agent.action_policy(current_state, env)
  if action is None:
    break

  current_state = env.state_transition(current_state, action)

print(f"Resultado SLS:\n{current_state}")

#ILS
greedy = SingleAgentSolver(env, GreedyAgent(evalConstructiveActions))
local_search = SingleAgentSolver(env, LocalSearchAgent(MoveType.SWAP, first_improvement=True))

initial_state = QAP_State(instance, matriz_asignacion=[0])

ils_solver = ILS_Solver(greedy, local_search, Perturbation(MoveType.SWAP, pert_size=2))
current_state, _, iterations = ils_solver.solve(initial_state, save_history=True, max_actions=100)
print(f"\nILS:\nIterations: {iterations}\n{current_state}\n")

# SciPy
res = quadratic_assignment(flow, distance)
print("Resultado FAQ:\n Costo:",res)
print("\n",random.choice(cats))

"""## Generador de instancias"""

import pandas as pd

class QAP_Instance_Generator:
  @staticmethod
  def generar_matrices(n, limite_flujo, limite_distancia):
    # Generar la parte triangular superior de la matriz
    matriz = np.random.randint(limite_flujo, limite_distancia + 1, size=(n, n))
    matriz = np.triu(matriz)

    # Hacer la matriz simétrica
    matriz += matriz.T - np.diag(np.diag(matriz))

    # Poner ceros en la diagonal principal
    np.fill_diagonal(matriz, 0)

    return matriz

  @staticmethod
  def generar_instancia(n, limite_flujo=1, limite_distancia=10, seed=None):
    if seed is not None:
        np.random.seed(seed)

    if n < 3:
      n = 3

    matriz_flujo = QAP_Instance_Generator.generar_matrices(n, 1, limite_flujo)
    matriz_distancia = QAP_Instance_Generator.generar_matrices(n, 1, limite_distancia)

    instance = QAP_Instance(matriz_flujo, matriz_distancia)
    return instance

"""## Comparaciones"""

from scipy.optimize import quadratic_assignment

def run_qap_algorithms(greedy, sls, ils, n=30, limite_flujo=1, limite_distancia=10): # Agregar TS
  resultados_greedy = []
  resultados_sls = []
  resultados_ils = []
  resultados_saipai = []
  #resultados_ts = []

  for i in range(10):
    print(f"Iteration {i+1} with size {n}")

    # Generar una nueva instancia del problema
    qap_instance = QAP_Instance_Generator.generar_instancia(n, limite_flujo, limite_distancia)

    current_state = QAP_State(qap_instance, matriz_asignacion=[0])

    # Greedy
    current_state, *_ = greedy.solve(current_state)
    resultados_greedy.append(current_state.costo)

    # Single Agent Local Search
    current_state, *_ = sls.solve(current_state)
    resultados_sls.append(current_state.costo)

    # Iterated Local Search
    current_state = QAP_State(qap_instance, matriz_asignacion=[0])
    current_state, *_ = ils.solve(current_state)
    resultados_ils.append(current_state.costo)

    # Saipai

    #current_state = QAP_State(qap_instance, matriz_asignacion=[0])
    #current_state, *_ = vns.solve(current_state)
    #resultados_ts.append(current_state.costo)

  return resultados_greedy, resultados_sls, resultados_ils # resultados_ts

def calcular_prom_resultados(greedy, sls, ils, sizes): # Agregar TS
  prom_resultados_greedy = []
  prom_resultados_sls = []
  prom_resultados_ils = []
  #prom_resultados_saipai = []
  #prom_resultados_ts = []

  for n in sizes:
    resultados_greedy, resultados_sls, resultados_ils = \
       run_qap_algorithms(greedy, sls, ils, n, limite_flujo=10, limite_distancia=100) # Agregar TS y en la anterior

    resultados_saipai = []
    prom_greedy = sum(resultados_greedy) / len(resultados_greedy)
    prom_sls = sum(resultados_sls) / len(resultados_sls)
    prom_ils = sum(resultados_ils) / len(resultados_ils)
    #prom_saipai = sum(resultados_saipai) / len(resultados_saipai)
    #prom_ts = sum(ts_results) / len(ts_results)

    prom_resultados_greedy.append(prom_greedy)
    prom_resultados_sls.append(prom_sls)
    prom_resultados_ils.append(prom_ils)
    #prom_resultados_saipai.append(prom_saipai)
    #prom_resultados_ts.append(prom_ts)

  return prom_resultados_greedy, prom_resultados_sls, prom_resultados_ils #prom_resultados_saipai, # prom_results_ts


sizes = [10, 20, 30, 40]
env = QAP_Environment

greedy = SingleAgentSolver(env, GreedyAgent(evalConstructiveActions))
local_search = SingleAgentSolver(env, LocalSearchAgent(MoveType.SWAP, first_improvement=True))
ils = ILS_Solver(greedy, local_search, Perturbation([MoveType.SWAP, MoveType.TWO_OPT, MoveType.RELOCATION], pert_size=2))

prom_resultados_greedy, prom_resultados_sls, prom_resultados_ils = \
  calcular_prom_resultados(greedy, local_search, ils, sizes) # Agregar TS aquí y arriba

"""## Graficar"""

import matplotlib.pyplot as plt

def plot_prom_resultados(greedy_resultados, sls_resultados, ils_resultados, sizes):
    # Crear un gráfico de líneas
    plt.figure(figsize=(8,8))
    plt.plot(sizes, prom_resultados_greedy, label="Greedy")
    plt.plot(sizes, prom_resultados_sls, label="SLS")
    plt.plot(sizes, prom_resultados_ils, label="ILS")

    #plt.plot(sizes, ts_resultados, label="TS")

    # Añadir títulos y etiquetas
    plt.title("costo QAP por algoritmo ")
    plt.xlabel("Cantidad de instancias")
    plt.ylabel("costo promedio")
    plt.legend()
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()


plot_prom_resultados(prom_resultados_greedy, prom_resultados_sls, prom_resultados_ils, sizes)