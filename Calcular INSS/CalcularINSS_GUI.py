import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def calcular_inss(salario):
    inss = 0
    if salario <= 1412.00:
        inss = salario * 0.075
    elif salario <= 2666.68:
        inss = (1412.00 * 0.075) + ((salario - 1412.00) * 0.09)
    elif salario <= 4000.03:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((salario - 2666.68) * 0.12)
    elif salario <= 7786.02:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((salario - 4000.03) * 0.14)
    else:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((7786.02 - 4000.03) * 0.14)
    return inss


def calcular_irrf(salario, inss, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario - inss - deducao_dependentes
    
    if base_calculo <= 2259.20:
        irrf = 0
    elif base_calculo <= 2826.65:
        irrf = (base_calculo * 0.075) - 169.44
    elif base_calculo <= 3751.05:
        irrf = (base_calculo * 0.15) - 381.44
    elif base_calculo <= 4664.68:
        irrf = (base_calculo * 0.225) - 662.77
    else:
        irrf = (base_calculo * 0.275) - 896.00
    return max(irrf, 0)


def calcular_fgts(salario):
    return salario * 0.08


class SistemaFolhaPagamento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cálculo - Folha de Pagamento")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        style = ttk.Style()
        style.theme_use('clam')
        
        self.funcionarios = {}
        self.tela_atual = "menu"
        self.mostrar_menu()
    
    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def mostrar_menu(self):
        self.tela_atual = "menu"
        self.limpar_tela()
        
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)

        titulo = ttk.Label(frame_principal, text="Sistema de RH - Folha de Pagamento", 
                          font=("Arial", 18, "bold"))
        titulo.pack(pady=20)
        
        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.pack(pady=30)
        
        botao_cadastrar = ttk.Button(frame_botoes, text="Cadastrar Novo Funcionário", 
                                    command=self.mostrar_cadastro, width=25)
        botao_cadastrar.pack(pady=10)
        
        botao_consultar = ttk.Button(frame_botoes, text="Consultar Funcionários", 
                                    command=self.mostrar_consulta, width=25)
        botao_consultar.pack(pady=10)
        
        botao_sair = ttk.Button(frame_botoes, text="Sair", 
                              command=self.root.quit, width=25)
        botao_sair.pack(pady=10)
        
        info = ttk.Label(frame_principal, 
                        text=f"Funcionários cadastrados: {len(self.funcionarios)}", 
                        font=("Arial", 10))
        info.pack(side=tk.BOTTOM, pady=10)
    
    def mostrar_cadastro(self):
        self.tela_atual = "cadastro"
        self.limpar_tela()
        
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = ttk.Label(frame_principal, text="Cadastro de Funcionário", 
                          font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        frame_form = ttk.LabelFrame(frame_principal, text="Dados do Funcionário", padding="15")
        frame_form.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.entry_nome = ttk.Entry(frame_form, width=40)
        self.entry_nome.grid(row=0, column=1, pady=10, padx=10)
        
        ttk.Label(frame_form, text="Cargo:").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_cargo = ttk.Entry(frame_form, width=40)
        self.entry_cargo.grid(row=1, column=1, pady=10, padx=10)

        ttk.Label(frame_form, text="Número de Dependentes:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.entry_dependentes = ttk.Spinbox(frame_form, from_=0, to=20, width=37)
        self.entry_dependentes.grid(row=2, column=1, pady=10, padx=10)
        self.entry_dependentes.set(0)
        
        ttk.Label(frame_form, text="Salário Bruto (R$):").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.entry_salario = ttk.Entry(frame_form, width=40)
        self.entry_salario.grid(row=3, column=1, pady=10, padx=10)
        
        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.pack(pady=20)
        
        botao_salvar = ttk.Button(frame_botoes, text="Cadastrar", 
                                 command=self.salvar_funcionario)
        botao_salvar.pack(side=tk.LEFT, padx=10)
        
        botao_voltar = ttk.Button(frame_botoes, text="Voltar", 
                                 command=self.mostrar_menu)
        botao_voltar.pack(side=tk.LEFT, padx=10)
        
        self.label_status = ttk.Label(frame_principal, text="", foreground="green")
        self.label_status.pack(pady=10)
    
    def salvar_funcionario(self):
        nome = self.entry_nome.get().strip()
        cargo = self.entry_cargo.get().strip()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, digite o nome do funcionário!")
            return
        
        if nome in self.funcionarios:
            messagebox.showerror("Erro", f"Já existe um funcionário cadastrado com o nome '{nome}'!")
            return
        
        if not cargo:
            messagebox.showerror("Erro", "Por favor, digite o cargo!")
            return
        
        try:
            dependentes = int(self.entry_dependentes.get())
            salario = float(self.entry_salario.get())
            
            if salario <= 0:
                messagebox.showerror("Erro", "O salário deve ser maior que zero!")
                return
            
            if dependentes < 0:
                messagebox.showerror("Erro", "O número de dependentes não pode ser negativo!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite valores válidos para dependentes e salário!")
            return
        
        inss = calcular_inss(salario)
        irrf = calcular_irrf(salario, inss, dependentes)
        fgts = calcular_fgts(salario)
        salario_liquido = salario - inss - irrf
        
        self.funcionarios[nome] = {
            'cargo': cargo,
            'dependentes': dependentes,
            'salario_bruto': salario,
            'inss': inss,
            'irrf': irrf,
            'fgts': fgts,
            'salario_liquido': salario_liquido
        }
        
        messagebox.showinfo("Sucesso", f"Funcionário '{nome}' cadastrado com sucesso!")
        
        self.entry_nome.delete(0, tk.END)
        self.entry_cargo.delete(0, tk.END)
        self.entry_dependentes.set(0)
        self.entry_salario.delete(0, tk.END)
        
        self.mostrar_menu()
    
    def mostrar_consulta(self):
        self.tela_atual = "consulta"
        self.limpar_tela()
        
        if not self.funcionarios:
            messagebox.showinfo("Informação", "Nenhum funcionário cadastrado!")
            self.mostrar_menu()
            return
        
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = ttk.Label(frame_principal, text="Consultar Funcionários", 
                          font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        frame_lista = ttk.LabelFrame(frame_principal, text="Funcionários (Ordem Alfabética)", padding="10")
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, height=15, font=("Arial", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        nomes_ordenados = sorted(self.funcionarios.keys())
        for nome in nomes_ordenados:
            cargo = self.funcionarios[nome]['cargo']
            self.listbox.insert(tk.END, f"{nome} - {cargo}")
        
        self.listbox.bind('<<ListboxSelect>>', self.on_selecionar_funcionario)
        
        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.pack(pady=20)
        
        botao_ver = ttk.Button(frame_botoes, text="Ver Holerite", 
                              command=self.ver_holerite)
        botao_ver.pack(side=tk.LEFT, padx=10)
        
        botao_voltar = ttk.Button(frame_botoes, text="Voltar", 
                                 command=self.mostrar_menu)
        botao_voltar.pack(side=tk.LEFT, padx=10)
    
    def on_selecionar_funcionario(self, event):
        self.indice_selecionado = self.listbox.curselection()
    
    def ver_holerite(self):
        if not hasattr(self, 'indice_selecionado') or not self.indice_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione um funcionário!")
            return
        
        indice = self.indice_selecionado[0]
        nomes_ordenados = sorted(self.funcionarios.keys())
        nome_selecionado = nomes_ordenados[indice]
        dados = self.funcionarios[nome_selecionado]
        
        self.mostrar_holerite(nome_selecionado, dados)
    
    def mostrar_holerite(self, nome, dados):
        self.tela_atual = "holerite"
        self.limpar_tela()
        
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = ttk.Label(frame_principal, text="CONTRACHEQUE (HOLERITE)", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        frame_holerite = ttk.LabelFrame(frame_principal, text="Detalhes do Holerite", padding="15")
        frame_holerite.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Label(frame_holerite, text=f"Funcionário: {nome}", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=5)
        ttk.Label(frame_holerite, text=f"Cargo: {dados['cargo']}").pack(anchor=tk.W)
        ttk.Label(frame_holerite, text=f"Dependentes: {dados['dependentes']}").pack(anchor=tk.W, pady=(0, 15))
        
        ttk.Separator(frame_holerite, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_holerite, text="PROVENTOS", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 5))
        ttk.Label(frame_holerite, text=f"Salário Bruto.................................... R$ {dados['salario_bruto']:>10.2f}").pack(anchor=tk.W)
        
        ttk.Separator(frame_holerite, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_holerite, text="DESCONTOS", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 5))
        ttk.Label(frame_holerite, text=f"INSS (Contribuição)........................... R$ {dados['inss']:>10.2f}").pack(anchor=tk.W)
        ttk.Label(frame_holerite, text=f"IRRF (Imposto de Renda)...................... R$ {dados['irrf']:>10.2f}").pack(anchor=tk.W)
        total_descontos = dados['inss'] + dados['irrf']
        ttk.Label(frame_holerite, text=f"Total de Descontos............................ R$ {total_descontos:>10.2f}", font=("Arial", 9, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        ttk.Separator(frame_holerite, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_holerite, text=f"SALÁRIO LÍQUIDO............................... R$ {dados['salario_liquido']:>10.2f}", 
                 font=("Arial", 11, "bold"), foreground="green").pack(anchor=tk.W, pady=10)
        
        ttk.Separator(frame_holerite, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_holerite, text="INFORMAÇÕES ADICIONAIS", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 5))
        ttk.Label(frame_holerite, text=f"FGTS (Fundo de Garantia 8%).................. R$ {dados['fgts']:>10.2f}").pack(anchor=tk.W, pady=(0, 10))
        
        ttk.Label(frame_holerite, text=f"Data de Emissão: {datetime.now().strftime('%d/%m/%Y')}").pack(anchor=tk.W, font=("Arial", 9))
        
        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.pack(pady=20)
        
        botao_voltar = ttk.Button(frame_botoes, text="Voltar", 
                                 command=self.mostrar_consulta)
        botao_voltar.pack(side=tk.LEFT, padx=10)
        
        botao_menu = ttk.Button(frame_botoes, text="Menu Principal", 
                               command=self.mostrar_menu)
        botao_menu.pack(side=tk.LEFT, padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaFolhaPagamento(root)
    root.mainloop()
