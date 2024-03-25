import streamlit as st
import pandas as pd

@st.cache_data 
def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)
    

st.set_page_config(page_title = 'Informativos do STF', \
        layout="wide",
        initial_sidebar_state='expanded'
    )

st.title('INFORMATIVOS STF')
st.markdown('Fonte: https://www.stf.jus.br/arquivo/cms/informativoSTF/anexo/Informativo_Dados/Dados_InformativosSTF.xlsx')

InformativosSTF= pd.read_excel('Dados_InformativosSTF.xlsx')
df= InformativosSTF.copy()
df=df.rename(columns = {'Classe Processo': 'Classe_Processo', 'Número Processo': 'Número_Processo', 
                                'Incidente Julgamento':'Incidente_Julgamento','Data Julgamento':'Data_Julgamento',
                                'Redator Acórdão':'Redator_Acórdão', 'Tipo Julgamento':'Tipo_Julgamento', 
                                'Situação Julgamento':'Situação_Julgamento', 'Tese Julgado':'Tese_Julgado',
                                'Ramo Direito':'Ramo_Direito', 'Repercussão Geral':'Repercussão_Geral',
                                'Tema RG':'Tema_RG', 'ODS ONU 2030':'ODS_ONU_2030', 'Notícia completa':'Notícia_Completa'
                                                 })
df['Incidente_Julgamento']=df['Incidente_Julgamento'].fillna(str('nan'))
df['UF']=df['UF'].fillna(str('nan'))
df['Observação']=df['Observação'].fillna(str('nan'))
df['Redator_Acórdão']=df['Redator_Acórdão'].fillna(str('nan'))
df['Título']=df['Título'].fillna(str('nan'))
df['Tese_Julgado']=df['Tese_Julgado'].fillna(str('nan'))
df['Resumo']=df['Resumo'].fillna(str('nan'))
df['Notícia']=df['Notícia'].fillna(str('nan'))
df['Ramo_Direito']=df['Ramo_Direito'].fillna(str('nan'))
df['Repercussão_Geral']=df['Repercussão_Geral'].fillna(str('nan'))
df['Tema_RG']=df['Tema_RG'].fillna(int(0))
df['Tema_RG']=df['Tema_RG'].astype(int)
df['Legislação']=df['Legislação'].fillna(str('nan'))
df['ODS_ONU_2030']=df['ODS_ONU_2030'].fillna(str('nan'))
df['Covid-19']=df['Covid-19'].fillna(str('nan'))
df['Legislação']=df['Legislação'].fillna(str('nan'))
df['Notícia_Completa']=df['Notícia_Completa'].fillna(str('nan'))  
df['Data_Julgamento'] =df['Data_Julgamento'].astype(str)
df[['Ano', 'Mês', 'Dia-hora']]=df['Data_Julgamento'].str.split('-', expand=True)
df[['Dia', 'Hora']] = df['Dia-hora'].str.split(' ', expand=True)
df = df.drop(['Dia-hora','Hora'], axis=1)
df['Informativo']=df['Informativo'].astype(str)
df['Informativo']=df['Informativo'].str.replace(',','')
df['Informativo']=df['Informativo'].astype(int)


df1 = df['Ramo_Direito'].astype(str)
df1=df1.str.split(";", expand=True)
columns=[0,1,2,3,4]
for i in columns:
    df1.loc[df1[i]=='Direito Constitucional', 'Direito_Constitucional']=True
    df1.loc[df1[i]=='Direito Processual Penal', 'Direito_Processual_Penal']=True
    df1.loc[df1[i]=='Direito Administrativo', 'Direito_Administrativo']=True
    df1.loc[df1[i]=='Direito Penal', 'Direito_Penal']=True
    df1.loc[df1[i]=='Direito Processual Civil', 'Direito_Processual_Civil']=True
    df1.loc[df1[i]=='Direito Tributário', 'Direito_Tributário']=True
    df1.loc[df1[i]=='Direito Previdenciário', 'Direito_Previdenciário']=True
    df1.loc[df1[i]=='Direito Eleitoral', 'Direito_Eleitoral']=True
    df1.loc[df1[i]=='Direito Internacional', 'Direito_Internacional']=True
    df1.loc[df1[i]=='Direito do Trabalho', 'Direito_Trabalho']=True
    df1.loc[df1[i]=='Direito Penal Militar', 'Direito_Penal_Militar']=True
    df1.loc[df1[i]=='Direito Processual Penal Militar', 'Direito_Processual_Penal_Militar']=True
    df1.loc[df1[i]=='Direito Civil', 'Direito_Civil']=True
    df1.loc[df1[i]=='Direito Financeiro', 'Direito_Financeiro']=True
    df1.loc[df1[i]=='Direito da Criança e do Adolescente', 'Direito_Criança_Adolescente']=True
    df1.loc[df1[i]=='Direito Ambiental', 'Direito_Ambiental']=True
    df1.loc[df1[i]=='Direito Processual do Trabalho', 'Direito_Processual_Trabalho']=True
    df1.loc[df1[i]=='Direito da Saúde', 'Direito_Saúde']=True
    df1.loc[df1[i]=='Direito do Consumidor', 'Direito_Consumidor']=True
    df1.loc[df1[i]=='Direito Monetário', 'Direito_Monetário']=True
    df1.loc[df1[i]=='Direito Comercial', 'Direito_Comercial']=True
    df1.loc[df1[i]=='Direito Empresarial', 'Direito_Empresarial']=True
    df1.loc[df1[i]=='Direito Agrário', 'Direito_Agrário']=True
    df1.loc[df1[i]=='Direito Notarial e Registral', 'Direito_Notarial_Registral']=True
    df1 = df1.drop([i], axis=1)
df1 = df1.fillna(False)
#df1 = df1.astype(int)
#df1 = df1.astype(str)
df1 = df1.reset_index(drop=False)
df1.rename(columns={'index':'Indice_Notícia'}, inplace=True)
df1['Indice_Notícia']=df1['Indice_Notícia']+1
#df1['Indice_Notícia']=df1['Indice_Notícia'].astype(str)
#df1['Indice_Notícia']=df1['Indice_Notícia'].str.replace(',','')


df2=pd.concat([df, df1], axis=1)
df3 = df2[[
       'Informativo','Indice_Notícia','Ano','Mês', 'Dia',
       'Direito_Constitucional', 'Direito_Administrativo','Direito_Tributário','Direito_Penal','Direito_Processual_Penal',
       'Direito_Previdenciário','Direito_Civil', 'Direito_Processual_Civil', 'Direito_Trabalho','Direito_Processual_Trabalho',
       'Direito_Internacional','Direito_Financeiro','Direito_Eleitoral','Direito_Criança_Adolescente','Direito_Ambiental',
       'Direito_Consumidor','Direito_Saúde','Direito_Monetário','Direito_Comercial','Direito_Empresarial', 'Direito_Agrário',
       'Direito_Notarial_Registral','Direito_Penal_Militar', 'Direito_Processual_Penal_Militar','Repercussão_Geral'
       ]]
st.markdown(' ')

with st.sidebar.form('my form'):
    st.header('Filtro')
    min_informativo = (df3.Informativo.min())
    max_informativo = (df3.Informativo.max())
    Informativo = st.slider(label = '**INFORMATIVO**',
                                    min_value = min_informativo,
                                    max_value = max_informativo,
                                    value = (min_informativo, max_informativo),
                                    step=1)
    st.write('*Informativo*:', Informativo)
    st.write('*Informativo Antigo:*', Informativo[0])
    st.write('*Informativo Recente:*', Informativo[1])
    df3 = df3[(df3['Informativo'] >= Informativo[0]) & (df3['Informativo'] <= Informativo[1])]


    ano_lista = df3.Ano.unique().tolist()
    ano_lista.append('all')
    ano_lista = sorted(ano_lista, reverse=True)
    ano_selected = st.multiselect('**ANO**', ano_lista,['all'])
    df3 = multiselect_filter(df3, 'Ano', ano_selected)
    
    mes_lista = df3.Mês.unique().tolist()
    mes_lista.append('all')
    mes_lista = sorted(mes_lista, reverse=True)
    mes_selected = st.multiselect('**MÊS**', mes_lista, ['all'])
    df3 = multiselect_filter(df3, 'Mês', mes_selected)

    cf_lista = df3.Repercussão_Geral.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**REPERCUSSÃO GERAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Repercussão_Geral', cf_selected)

    cf_lista = df3.Direito_Constitucional.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO CONSTITUCIONAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Constitucional', cf_selected)
    
    cf_lista = df3.Direito_Administrativo.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO ADMINISTRATIVO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Administrativo', cf_selected)

    cf_lista = df3.Direito_Tributário.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO TRIBUTÁRIO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Tributário', cf_selected)
    
    cf_lista = df3.Direito_Penal.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PENAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Penal', cf_selected)

    cf_lista = df3.Direito_Processual_Penal.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PROCESSO PENAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Processual_Penal', cf_selected)

    cf_lista = df3.Direito_Previdenciário.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PREVIDENCIÁRIO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Previdenciário', cf_selected)
    
    cf_lista = df3.Direito_Civil.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO CIVIL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Civil', cf_selected)

    cf_lista = df3.Direito_Processual_Civil.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PROCESSO CIVL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Processual_Civil', cf_selected)

    cf_lista = df3.Direito_Trabalho.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO TRABALHO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Trabalho', cf_selected)
    
    cf_lista = df3.Direito_Processual_Trabalho.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PROCESSO TRABALHO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Processual_Trabalho', cf_selected)

    cf_lista = df3.Direito_Internacional.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO INTERNACIONAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Internacional', cf_selected)

    cf_lista = df3.Direito_Financeiro.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO FINANCEIRO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Financeiro', cf_selected)

    cf_lista = df3.Direito_Eleitoral.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO ELEITORAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Eleitoral', cf_selected)

    cf_lista = df3.Direito_Criança_Adolescente.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO CRIANÇA ADOLESCENTE**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Criança_Adolescente', cf_selected)

    cf_lista = df3.Direito_Ambiental.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO AMBIENTAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Ambiental', cf_selected)

    cf_lista = df3.Direito_Consumidor.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO CONSUMIDOR**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Consumidor', cf_selected)

    cf_lista = df3.Direito_Saúde.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO SAÚDE**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Saúde', cf_selected)

    cf_lista = df3.Direito_Monetário.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO MONETÁRIO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_MOnetário', cf_selected)

    cf_lista = df3.Direito_Comercial.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO COMERCIAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Comercial', cf_selected)

    cf_lista = df3.Direito_Empresarial.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO EMPRESARIAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Empresarial', cf_selected)

    cf_lista = df3.Direito_Agrário.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO AGRÁRIO**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Agrário', cf_selected)

    cf_lista = df3.Direito_Notarial_Registral.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO NOTARIAL**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Notarial_Registral', cf_selected)

    cf_lista = df3.Direito_Penal_Militar.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PENAL MILITAR**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Penal_Militar', cf_selected)

    cf_lista = df3.Direito_Processual_Penal_Militar.unique().tolist()
    cf_lista.append('all')
    cf_selected = st.multiselect('**DIREITO PROCESSO PENAL MILITAR**', cf_lista, ['all'])
    df3 = multiselect_filter(df3, 'Direito_Processual_Penal_Militar', cf_selected)
    
    st.form_submit_button(label='Aplicar')

st.write(df3)

st.markdown(f'''TOTAL DE LINHAS DO DATAFRAME: :blue[{df3.Indice_Notícia.value_counts().sum()}] .''')
st.markdown('')
st.subheader('LEITURA DA NOTÍCIA - CONTEÚDO')
st.markdown('')
st.markdown('')
st.markdown('Para proceder com a leitura da notícia, preencha o campo abaixo com o número da notícia desejada constante na coluna :violet[Indice_Notícia]:')

#I_N_lista = { }
#
# st.I_N_selected = st.multiselect('**Índice da Notícia**', I_N_lista)


number = st.number_input('**Índice_Notícia**', min_value=df3.Indice_Notícia.min(), max_value=df3.Indice_Notícia.max(), value='min')

if number in df3.Indice_Notícia.values:
    df_number= df2[df2['Indice_Notícia']==number]
    #df_number
    df_Inf =df_number.loc[number-1:number-1, 'Informativo']
    df_CP = df_number.loc[number-1:number-1, 'Classe_Processo']
    df_NP = df_number.loc[number-1:number-1, 'Número_Processo']
    df_UF = df_number.loc[number-1:number-1, 'UF']
    df_d = df_number.loc[number-1:number-1, 'Dia']
    df_m = df_number.loc[number-1:number-1, 'Mês']
    df_a = df_number.loc[number-1:number-1, 'Ano']
    df_R = df_number.loc[number-1:number-1, 'Relator']
    df_RA = df_number.loc[number-1:number-1, 'Redator_Acórdão']
    df_OJ = df_number.loc[number-1:number-1, 'Órgão Julgador']
    df_TJ = df_number.loc[number-1:number-1, 'Tipo_Julgamento']
    df_SJ = df_number.loc[number-1:number-1, 'Situação_Julgamento']
    df_RG = df_number.loc[number-1:number-1, 'Repercussão_Geral']
    df_T = df_number.loc[number-1:number-1, 'Título']
    df_Te = df_number.loc[number-1:number-1, 'Tese_Julgado']
    df_Re = df_number.loc[number-1:number-1, 'Resumo']
    df_No= df_number.loc[number-1:number-1, 'Notícia']
    df_RD = df_number.loc[number-1:number-1, 'Ramo_Direito']
    df_Ma = df_number.loc[number-1:number-1, 'Matéria']
    df_Le = df_number.loc[number-1:number-1, 'Legislação']
    container =  st.container(border=True)
    col1, col2, col3 = container.columns(3)
    with col1:
        st.write(f'INFORMATIVO: :orange[{df_Inf.values[0]}]')
        st.write(f'PROCESSO: :orange[{df_CP.values[0]} {df_NP.values[0]} / {df_UF.values[0]}]')
        st.write(f'DATA DO JULGAMENTO: :orange[{df_d.values[0]}/{df_m.values[0]}/{df_a.values[0]}]')
    with col2:
        st.write(f'RELATOR: :orange[{df_R.values[0]}]')
        st.write(f'REDATOR ACÓRDÃO: :orange[{df_RA.values[0]}]')
        st.write(f'ÓRGÃO JULGADOR: :orange[{df_OJ.values[0]}]')
    with col3:
        st.write(f'TIPO DE JULGAMENTO: :orange[{df_TJ.values[0]}]')
        st.write(f'SITUAÇÃO DO JULGAMENTO: :orange[{df_SJ.values[0]}]')
        st.write(f'REPERCUSSÃO GERAL: :orange[{df_RG.values[0]}]')
    st.subheader(f'TÍTULO: {df_T.values[0]}')
    st.markdown(' ')
    st.markdown(f':orange[**TESE:**] {df_Te.values[0]}')
    st.markdown(f':orange[**RESUMO:**] {df_Re.values[0]}')
    st.markdown(f':orange[**Notícia:**] {df_No.values[0]}')
    st.markdown(f':orange[**Ramo do Direito:**] {df_RD.values[0]}')
    st.markdown(f':orange[**Matéria:**] {df_Ma.values[0]}')
    st.markdown(f':orange[**Legislação:**] {df_Le.values[0]}')
else:
   st.write('NOTÍCIA NÃO SELECIONADA')
