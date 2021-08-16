from tkinter import *
from tkinter import ttk
from time import sleep
from threading import Thread

import psutil


class SecundaryTh(Thread):

    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        while True:
            update_process_list()
            sleep(5)


def get_proc_infos(process_filter):
    """ Captura informações (ppid, pid, nome, % CPU, prioridade e status) dos
    processos e retorna na forma de uma lista de dicionários. """

    attrs = ['ppid','pid', 'cpu_percent', 'nice', 'status', 'name']

    if len(process_filter.get()):
        processes = []
        for p in psutil.process_iter(attrs):
            if process_filter.get() in p.info['name'] or process_filter.get() in str(p.info['pid']):
                processes.append(p.info)

    else:
        processes = [p.info for p in psutil.process_iter(attrs)]

    def sort_func(proc): return proc['cpu_percent']

    processes.sort(key=sort_func, reverse=True)

    procs = []
    for p in processes:
        proc = []
        proc.append(str(p['ppid']))
        proc.append(str(p['pid']))
        proc.append(str(p['cpu_percent']/psutil.cpu_count()))
        proc.append(str(p['status']))
        proc.append(str(p['nice']))
        proc.append(str(p['name']))
        procs.append(proc)

    return procs


def kill_proc():
    """ Mata o processo ativo (em destaque na interface).

    Exceptions:
        NoSuchProcess: quando o processo referente ao pid não é
        encontrado. """

    pid = get_current_process()
    p = psutil.Process(pid)
    p.terminate()


def suspend_proc():
    """ Suspende o processo ativo (em destaque na interface).

    Exceptions:
        NoSuchProcess: quando o processo referente ao pid não é
        encontrado. """

    pid = get_current_process()
    p = psutil.Process(pid)
    p.suspend()


def resume_proc():
    """ Retoma o processo ativo (em destaque na interface).

    Exceptions:
        NoSuchProcess: quando o processo referente ao pid não é
        encontrado. """

    pid = get_current_process()
    p = psutil.Process(pid)
    p.resume()


def set_proc_cpu(*args):
    """ Define em qual CPU o processo deve ser executado.

    Parâmetros:
        cpus: list com os índices das cpus nas quais se deseja que o processo
        seja executado.

    Exceptions:
        NoSuchProcess: quando o processo referente ao pid não é
        encontrado. """

    cpus = [int(i) - 1 for i in cpu_list.get().split(',')]
    print(cpus)

    pid = get_current_process()
    p = psutil.Process(pid)
    p.cpu_affinity(cpus)


def decrease_priority():
    """ Altera prioridade do processo ativo (em destaque na interface).

    Exceptions:
        NoSuchProcess: quando o processo referente ao pid não é encontrado.

        AccessDenied: quando o sistema não tem permissão pra alterar prioridade
        do processo. """

    print('Diminuindo prioridade do processo')
    pid = get_current_process()
    p = psutil.Process(pid)
    p.nice(p.nice() + 1)


def increase_priority():
    """ Altera prioridade do processo ativo (em destaque na interface).

    Exceptions:
        NoSuchProcess: quando o processo referente ao pid não é encontrado.

        AccessDenied: quando o sistema não tem permissão pra alterar prioridade
        do processo. """

    print('Aumentando prioridade do processo')
    pid = get_current_process()
    p = psutil.Process(pid)
    p.nice(p.nice() - 1)


def get_current_process():
    """ Captura e retorna id do processo ativo (em destaque na interface). """

    return process_list.item(process_list.focus())['values'][1]


def update_process_list():
    process_list.delete(*process_list.get_children())
    procs = get_proc_infos(process_filter)
    [process_list.insert('', 'end', values=p) for p in procs]

    try:
        process_list.focus(process_list.get_children()[1])
        process_list.selection_set(process_list.get_children()[1])

    except:
        pass


if __name__ == '__main__':

    root = Tk()
    update_thread = SecundaryTh(1)
    root.title("Gerenciador de Processos")

    main_frame = ttk.Frame(root, padding=20)
    process_frame = ttk.Frame(main_frame, padding=10)
    options_frame = ttk.Frame(main_frame, padding=10)

    process_list = ttk.Treeview(
        process_frame,
        columns=('ppid', 'pid', 'cpu_percent', 'status', 'nice', 'name'),
        show='headings',
        height=30,
        takefocus=True
    )
    process_list.heading('ppid', text='ppid')
    process_list.heading('pid', text='pid')
    process_list.heading('cpu_percent', text='% CPU')
    process_list.heading('nice', text='Prioridade')
    process_list.heading('status', text='Status')
    process_list.heading('name', text='Nome')

    process_filter = StringVar()
    filter_label = ttk.Label(options_frame, text='Filtro:')
    entry_process_filter = ttk.Entry(
        options_frame, textvariable=process_filter)

    cpu_list = StringVar()
    cpu_list.trace_add('write', set_proc_cpu)
    cpu_label = ttk.Label(options_frame, text='CPUs:')
    entry_cpus = ttk.Entry(options_frame, textvariable=cpu_list)

    btn_kill = ttk.Button(options_frame, text='Finalizar', command=kill_proc)
    btn_suspend = ttk.Button(
        options_frame, text='Suspender', command=suspend_proc)
    btn_resume = ttk.Button(options_frame, text='Retomar', command=resume_proc)
    btn_decrease_nice = ttk.Button(
        options_frame, text='- Prioridade', command=decrease_priority)
    btn_increase_nice = ttk.Button(
        options_frame, text='+ Prioridade', command=increase_priority)

    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    process_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    options_frame.grid(column=0, row=2, sticky=(N, W, E, S))

    process_list.grid(column=0, row=0, sticky=(N, W, E, S))

    filter_label.grid(column=0, row=0, padx=5, pady=5, sticky=(N, E, S))
    entry_process_filter.grid(column=1, row=0, padx=5,
                              pady=5, sticky=(N, W, E, S))
    cpu_label.grid(column=2, row=0, padx=5, pady=5, sticky=(N, E, S))
    entry_cpus.grid(column=3, row=0, padx=5, pady=5, sticky=(N, W, E, S))

    btn_kill.grid(column=4, row=0, padx=5, pady=5, sticky=(N, W, E, S))
    btn_suspend.grid(column=5, row=0, padx=5, pady=5, sticky=(N, W, E, S))
    btn_resume.grid(column=6, row=0, padx=5, pady=5, sticky=(N, W, E, S))
    btn_decrease_nice.grid(column=7, row=0, padx=5,
                           pady=5, sticky=(N, W, E, S))
    btn_increase_nice.grid(column=8, row=0, padx=5, pady=5, sticky=(N, E, S))

    update_thread.start()
    root.mainloop()
