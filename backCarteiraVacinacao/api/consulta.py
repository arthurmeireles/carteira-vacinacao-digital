from django.db import connection



class SqlBloc:

    @staticmethod
    def relatorio_vacinas_aplicadas_em_todos_estabelecimentos():
        sql = f"""
            SELECT
                date_trunc('day',"data_aplicacao") as dia,
                estabelecimento_id,
                vacina_id,
                count(*) as quantidade
            FROM public.api_aplicacao
            GROUP BY
                date_trunc('day',"data_aplicacao"),
                estabelecimento_id,
                vacina_id
            """
        cursor = connection.cursor()

        cursor.execute(sql)

        return SqlBloc.dictfetchall(cursor)

    @staticmethod
    def dictfetchall(cursor):
        """
        Pega os resultados de uma query executada através do cursor (que seria uma lista de tuplas)
        e transforma em uma lista de dicionários, onde a chave é o nome da coluna
        :param cursor:  cursor através do qual a query foi executada
        :return:        lista de dicionários
        """
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]