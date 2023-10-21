from fastapi import status
from core.configs import settings
from fastapi.testclient import TestClient
from main import app

# Intanciando um objeto do tipo TesteClient
client = TestClient(app)

PREFIX = settings.API_V1_STR


def test_response_root():
    """Função que testa a resposta do endpoint Get raiz

    Return: Deve retornar o True no caso do status_code ser 200
    """
    
    response = client.get(PREFIX)
    
    assert response.status_code == status.HTTP_200_OK

 
def test_create_user():
    """Função que testa o endpoint para criar usuário.

    Return: Deve retornar sucesso no caso do status_code ser 201
    """
    json_request_user = {
        "nome": "Teste de Criação de Usuário"
    }
    response = client.post(PREFIX + '/users', json=json_request_user)
    
    assert response.status_code == status.HTTP_201_CREATED

   
def test_update_user():
    """Função que testa o endpoint para fazer update do usuário.

    Return: Deve retornar sucesso no caso do status_code ser 201
    """
    json_request_user_update = {
        "user_id": 39,
        "nome": "Teste de atualização de Usuário"
    }
    
    response = client.post(PREFIX + '/users', json=json_request_user_update)

    assert response.status_code == status.HTTP_201_CREATED


def test_get_user_image():
    """Função que testa o endpoint que busca uma imagem relacionada à um usuário
        
    Return: Deve retornar True no caso do status_code ser 200
    """
    
    json_request_get_image = {
        "user_id": 10,
        "image_id": 20
    }
    
    response = client.get(PREFIX + '/users-images', json=json_request_get_image)
    
    if(response.status_code == status.HTTP_200_OK
       or response.status_code == status.HTTP_404_NOT_FOUND):
        assert True
        
    else:
        assert False

def test_create_user_image():
    """Função que testa o endpoint que cadastra uma imagem relacionada à um usuário
    
    Return: Deve retornar True no caso do status_code ser 201
    """
    
    json_request_create_user_image = {
        "user_id": 10,
        "b64image": "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABUAGMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD8w4viD8TvhgZzrnjjxt5m8oL3+27w2gjG0Da5fCgnB+facuF5K1s6J+0v8QNA1i3ux418YSG3fc0b61c4dejLy5xkEjOOOtemHMbd1IP4g1xev/A3SNQUtpudDk4wlqg+zdv+WP3V4z/q9mWYs241/pBiPCeeWRjLJbTjF3SdlNdV7z92Tv35LW6n9L1eDnhrSwNmlqk7J/fs368p6npn7QnizWbYTWvjbxNMjIr/AC6xOSgYZG4b8g+x9D6VY/4Xh41/6HDxV/4Nrj/4uvnyT4N+JdLlie0n0ueTdu3JPJbGEjGDna2T9MYx78WLbxx4z8MeUL/R9WnjYgIpsvtjFV6/NbGQqSCOZOT2zhq+qocTww6tm2Xypd5KF4L1drK+ltXrpvoexDM409MZhnHz5br77WX3vse9/wDC7/Gv/Q4eKv8AwbXH/wAXWLD8cvG+o/Ev5fGPi0RaRp3lsRrFwUmkuZQxU/PgPGtqhxySLoH5Rjd5nYfFLxHqysbTwdqcvlkB/NRrPbnpj7R5e7ofu5x3xkZ6fwLptzaaYbi/iWLUtUna+vEVgfKdgqpFkfKTHCkURZeG8rdyWJPq0sRl+b1qVLB0m6afPKTpuMGo/ClJxSb5+V2i9oSUn9l9tKeFxc4xow91O7fK0nbZJtavms9OzT7P7g/ZK1XxR8ZP+CZPhDRJvGniOwvfFWgeJNLbVTfTzTWrTa7rVus+PMUu0YKkDcPuAbh1HrHwq+Pev/FX4a6B4lfUNb0yfXdPhvLnTzqk0raZO6AzWrtlT5kMu+JwVUho2BVSCB5R/wAE7eP2BfhR/wBeut/+pNrFa2k3es/B7xV4j0218IeIvEOgapqL65pcukyWW2ye7JkvLaT7TcxSFze/aLrd8y4vwi7ViCj+PuAaUKeV08Q4XUp4iLsr7Yiq4vRN2XvLTuvl+YYWnCNKnO32Utvu/X70ew/8J5r3/Qd1v/wPm/8AiqP+E817/oO63/4Hzf8AxVeYf8NGeHM/8ePxBx6/8K88Q/8AyDSt8S/Fepf8g34c6rEYj+9Gt6vZ2O7PTyjA9zv6Hdu2Y+XG7J2/erFYGX8O0v8ACub77J2+Z181HpZ+iv8Alc9O/wCE817/AKDut/8AgfN/8VWH46+Pq+AbBF8QeKruGPVYpoI7K4uprl9TjKhJkS2UtJOoST94ERtqMS2BzXGjw54/8RkRal4j0Xw9bqfmk8P2Rmu5u42yXYeOLBAzmGTcruPkIVhs+CvhboHw8mup9J05Yr6+2fbNRuZ5b3Ur/YGEf2i8nZ7ifYrFE82RtiYRcKAoyr4aOLpyoOhHkkmpc8U001Zrk+0nqmnZeouXm0UUvX/L/hj9N/8Agkh4ZtPCP7APgu00+fxFLp7Xes3VpFron/tDT4ZtYvZo7OR55JJZfs6yLAsztmVYVkwu/aCqv7DP7Q/gDwN+yz4X0vW/HPg/R9TtftfnWd9rNtbzw7rudl3I7hhlWUjI5BB70V/HWZ5V9QxlXA03KUaUpQTlrJqLaTk+rdrt9Wfi2Y0eTF1YRWilJfifzWeC/iFc6jolhH4xl8lrtf8AQvENw5xnokV+x5AYAbbo5wWXziULzQdBqOnz6Tevb3MTwzxkbkYYIyMg/Qggg9wQaqGwg+w/ZvJiNvsEflFRs2gYAx0xXL6/8Y9c+AvxH8T+ENFvI9Z8KeH9Tm0hNH8R2wv7SOa2R7S4MRUxzwx/avtUkJhmjfYYPML7Ctf6Y4vNq/CPsMJO+IpTTtG6U4cqXNyt2UoXatFtON7JuNlH+nq2Lnk6p0ZXqQktF9qNrXs3o467OzV7arbrJJViALEAFgoz3JIAH5kURuJowyEOp6FTkGqEXxz8D+MLtCtlrPgq4nLF4bqddT02FjI21EuEVJggQpkywjbtfLt8udDW/guNZ8K/27Bbi80Qu0K6rpN15ltG+2MgO0ZIR8SREJKAw3jK8kV9LgOM8DmFo5fUi6j+xNunL5Jp3+Sa8z08PneHxK/2aScv5ZXi/wAV+nzCszxtMlv4N1UyMqKbSVMscAllKqPqSQB7msy68I61Z3DSaf4guDuwuy9QShV7nOMZyP7o4J59eZ8V6f4yv9LMF4v2m2b55Et1T+HB52gE+oHOSKM5z3EUsLUpzwlTmaaTSUo66JtxbsvkGNx9SFKSdGV7O1rNfNp/ofpl/wAE/LaV/wDgl18F5wjmCK+8Txs+PlRm1++Kg+5CNj/dPpXo1Vf+CTcGgN/wSw+Gtp4oNvDbPqGv7EuHaJ1lXxBqf3duGBAyCR2Yg9cHvtaT4dQ3Ae0fxbcJMzMY4GiRbcZ4Ueam4jkgZJPy8mv8ufAnxfqUKWY8M1MnxlR4fHY9RrU6DlQnGeMr1P4jkkpRlKcWnZe6ldydj8/w9L/Z6buvhX5HF0Vr6jq+marb2tlpnhxbS9mKxCVr+e7uJ3yoGxBsTcxyCAhzv+ULgV5X8V/2nvAvwX1dNJ1fWxf+J5p/skHhvQ4/7T1ie4LOiwGGM4ilMiGIpKyMsjKGVQwNf1B/rlhaGHVbNqc8LNuVqVR051ZKP2oxoVK3Mnvo20viUSatSFNXnLQ72uZ+KPxW034UaPazXUNzqmq6sxi0bQ7Fh9v1uUHaRHwwihU/6y4ZSsYBCrNKY4JTwh4J+OP7Q6WsvhbwrYfB3w1c+XI+v+NYYtU1+SJhbSZttKXdawNsknUi6NyH2jBtJBmuB/Z9+H2pfDP49/Frwx4u1q48deN/Bmq2tjP4uvZHe61KyurRLyziw5YxmK2miRgGOX3jLKoZvznhnxt4d4y4ircKZBi4qpSpyqzaadRwjOEHyJKUINuov4slVhrfD/aSpzc9XFqPe1r7aK+v3rpfU+ZP2kP+CVPxO/af+M+s+O9R8T/D3RLvX/IkfT47S5ZbIRwRxLFuXcG2rGBu3MWxksxJYlfoNDpV3cxh47S6kQ9GSFmB/ECivvqvCOTObfNJa7e0k7eV5Nyfzbfdtnm1ciwlSbqOLu3fd/5n51fCzw5b+Mfif4b0i78z7Jquq2tnN5Zw+ySZUbacHBwTjisf9qP9hzxP4r/Zs0j48+BtTF1qmv6AvjjxfoF4IhC0l5AdQvLizbCsqI00jCBmLbUG1nb5Gt6ZM+l+EPG+qpcJZnR/COsSxXJlETwXUtlLbWZjOQfON5cWyx7fmDuhGMZHvPwB/wCCoWka9pNvH4h8GXHhSzsBHaQ3fh8m+soWjiBP+iqiT28efLWKOEXO0MQ7Ise9vjvptY/xGhmeVVfD3D1a/wBUjUqV40nduM3FKLpr3535G3yKXLo2tmfacS0qeMxX1WUmnGF043um3vp25bu+jW5qfBr/AINqvGn7TH7KegfFX4T/ABs+HfxA0zxdp8GpaLBNps2l+ajuqyQTyxzXKwTwHzVlj2uVlheI4ILD40/bz/Z3+If/AAR7/aA0zwh451j+wvGGv+HY9YivPBWt3QD2Et1PEIZLhVt5M+baMxjwU4jbJPC/qJ+zt8av7ItZ4vg18WdX0bSrW++3JovhzUoG0iznRIVYrYmMosTFY2kRQI3eSRiN0rk6X7S//CT/ALZ2j6XYfFjXfD3xBs9Dne406PWfBelTGykdQrmNhEGXcAu4A4O1cg7Rj+RcJ9Lylh4fVs1c4VI25qdajdp2V9UuZ26Xtfsrn5p/YnEMHanOFWGttn997fmz8vF+IvjHw94H0nxN4++HPiJfC/iDyf7L8T/8I9P4dg1QzRPNCIZDbpYzmSNdyCFEJjjd8SHc9X9O8f8AgnXXRbbxWmnSSP5UcOt6dPZF24wxmjE1rFGcgeZNPGFwxfYgDn9Afjl+1bp/7Mf7Nej/AA/8b69pl18PbJY4NA8IaR4T0u2mg2SjzHt1REIRomuIZ2dwssV3cIzM0uG/K340fEG0+K3xV1vxDp2hWPhm01W486LTLI5itRtA64ALMQWYgKu5m2qowo/rnwG+kDxXxRTqVaNOX1NK8K84SVKcuazpxhVnKs+VfbjUdO6cbRaSf1mXZpm+Fp8teaT/AJb89l67/LmP0j+F/wC1b8Lvhl+y/wDDyw134q+Ao5NJs7u1ntNO1tNdntZ5dSvpubbTvtMyK0JiJmMYj/1as4YopWH9s2x8cQ27fD/wl4h8VQXWqDR7fWdZQ6Dod3dl4gtvasRJd39zLHIZIrK2g+3SAJttXLFF9t/Ym/Y5+A3jz9nv4aeIIPBfgbXPElv4a0TUtRuEK3csV5JZxSmSZN5AZpA5w64JDDHBFfQl74Ut9E1DR7gLaWUvh3zV0DUhYW8yaNuwYYGikRoxFDNHazwjHliWxtCwDQRl/wCEeLvpuQw+bYnJ8up1oJ4mvKq+WFJRVWvUqTcIwdSrN3m2nGvRk9HZ6ojE0MdWpSxFOUbyu1bu9bO97H5QeL/2tvA+ofEOHwh8bfjv40S/v7u58O6v4A+HOj3Xg3TtMlbNrLbavcap9jaSN2KMwvWljh/0tG8mNjn9Qf2Nf2OfEOi/DrTv+FNfCb4Y/D7wf4nsbfUrPW5NckvXurWRXuLVrjyYD9sO2VlUxX08cXm/u5ZIgu/k/jB+whpP7QHxmh+IXji90DxT44tzblda1HwNoktyxtyDCX/0fbJswAN6t8qhTlQAPYfEPiL4m6xpEr+Jfjf4y/sqxU3Uktjb6dopg2qcvJPBAp8sKXyrHb0Y8qK/G+JvFvw8z2rKec43EYmlJ80qKjOCqSTvFy9m6Mak1ouev7So9b1G25Hzccu4hV5QjGEn9q6dvVy5n6Wf+R8Xftj+O/2p9G/bsi/Zw+HPxU+Ed34pudMPifxRqmleGwD8ONLNzD5CSNcXUwuLuRHA8lrdWMc8Eg2rL5kWPrPgG9+C/wDwUJ8T6Bc+J9Z8WXfif4f6P4p1zVdUhtYZ9S1Jbi40wSBLeKOOKMW1hEFjVeMuWZyQR9L6P8WfBHwn0XUtR8Nx+IviLrOtalcrquqWXlXd/qt1HL5ri91O5eC2URrdkQfaLiNPLHk2+dqx18TfHH9rDU/ip/wUv8B2Pijwv4d8IN4N/t7wjLLpuoy6q2qX7SRxxK1y9vbs0f7ucwxmEGMNcuWxIyp+tfRLpZrmPilTzfhfJPquT06VaFSXLCE5RlFRhKbl+8mnW9iuSDlGErSd2mz3stwVenSUsRVdWpvKzbik00kul+Zrpf5HfePv2arP4geLbvV5fFvj/THu9mbbTdcltrWLaip8kY4XO3J9SSe9Fek0V/qbUyPKqk3UqYSjKT1bdGk231bbjdt9W9WdWn8q/wDAV/kfmJ8XdetfCf7NPiqe4+0STeIdW0Lw1apGg2xySX66gZXYkEKE0t0wASWlXoAa4v4DTDdq0ZfkiJlQt1++CQPxXJ+lRftca9d+G/2WrSzvhF9t1XxXFqOmXMByJP7LsbgTtIhH7tg+q2ewAuGxLnaFAah8HLyOy8dNEQc3NvLDHgdwVfn2wh/HFfcYXPVX8Qa76QdKFmrW5qbTT81JvunpZtWZ6lLH8/Ec/wC7yx7WvF6fe3+mh6jc6dDevvljV3xt34+bHpnrj26V6N4L/a1+J/w/QR2nipdctURkjtfE1n/aiR7n3l/PV4bx3zkDzbl0VWKhMCPZ5/RX3nHvhBwVxrRVHirLKOKttKcFzrp7tRWnH5SXTsfc1sDh6r5px17q6f3qz/E4b4ieFPG/xf8AHd7rniXxFY6jfXrkyXskcjttGdoWAbUROgEauFQHAzjmxpXwK0CxYNdLe6w4Jx9vm3JjGApijCQtjkgshbJ68LjsaK78n8N+Hstpxo4fDrkgkoxesIxWkVGHwJR6aXXfY4aGQYGm+bk5n/e1/B6fPfzPtj9jfT9P1v8AY5+G8s2lWMV/bt4gMepae02lamgHiHVLZQt5ZyQ3EeIreNCY5FLKXVy6uVr2zwp8UfGfgh9ll4mk8QafsEf9k+LlS5ijRVKpHBqFtCt3Gqg/M96mpzT7Iw0sTGWeTxb9iD/kzf4ffXxB/wCpTrVeo1/ntiPo9cBca5dXxGfYCMq9Svim6sW41OZ4qs3K97OTu1zSTaVknaMbfnsd/aJ2l3/z7/O50Q+O3xEjIWz1bwDoFsnC2Q8P33iRF91uHvdMZF7CIwvtxkTEMIouaeJ7vWV1TUL7WPEWtKkka6nrt2l5cRrJGYnWKKOOKytQ8R8txZ2tuJlAM3mvmQv6UV6XBX0VvDXhjFLG4LL41KqVlKr+8fq01yybdneSbuk1Zq42ub43f1/y2XyQl/M91FmRi/lR+XHnpEgzhVHRVGeAOB2r8/8A9tv4iR/Cf9vibxBJbSXq6f8AF+72wqwUyO8t/GoJ7DcwyecDOAelfoLZ6Zca3ew2VpH513eSLBBGGC+ZI5CqMkgDJI5JAr8sv+CkHxB07xR+1BqevWN39s8Nz+K9U8VQTJEymeKHUYJElVWCtk280wCtjmTkAgEfuNOpDB4yVSjFKNHDu9lpDnxOF9ne2kVL2c+XbmUJ8t+V276Nb2OFrVuyj/6XGx+pUieXIy+hxRWb4Q8Unxx4W0/Wf7Pk0pdVt0u0tZLtbp4kkAZcyKiAkqQeFGM45xklelRm504zlFxbSdmrNeTXRrqu5xarRn5Pft12hPwV+GHmxt5dxq/iXbuUgSL5OhqceoyCPwNcF8CfFhn1fSbm4IknhuDZXDFtvzMNgcnpnY6OccZJHHbo/wBvq4kfxJ8Noi7mKPwUHVCflVm1vVwxA7EhVz67R6V434K1ldD1wiZxHaXcZjlLY2o45RmPYY3qf99c8DI+RzLiCWD45xeO2Xtmn6wajF/fG+uiUnueHjMydHiCriNlz2/8Bsk/vXyTZ9iUVyPwt8eHxDZ/Yb2Q/wBo244Z2GbleeR0+ZQMH8+ecddX9lZVmdDMMNHFYd6P70+qfmv+CtD9rwmKp4mkq1PZ/h5MKKKK9E6T7c/Yg/5M3+H318Qf+pTrVeoV5f8AsQf8mb/D76+IP/Up1qvUK/ibgX/kVy/6/Yn/ANSap+SQ2CiikZtoyeBX2JZQ8aeNT8Mfhx4q8Uo0yTeHNHnubZ4FDSwXUpS0tJlBIH7u6ubeQknhY2IDEBW/GX4+eIj4nn8SuGDWulWl1p1rgEYKpickHncZlZD2IgQjrlv0I/4KnftGw/D34XJ8P9KvIv8AhI9Qm+334Uq72NxGskNtAVzjMXnST3COrAZtl+WRWQ/nfb28cISJAfKUBQGJYke5OST6k8nvXzuGUsVQxM07LEONn3pU4tUrq+qdSdeqn9qEqE4uzRWNv9V+qrRy1fptFfnL/wABaP2P+D8yS/CPwqUdXA0ezUlSDgiBAR9QQQfcUV5F/wAE9U8S3f7FHw3ltNf0y2gk0aNhHcaBDdyAktuLSs4ZiWyeR3x2orPGcQ5lLETlSy6pKLbs+elqr6PWaevmk+6M6tdzm5KD1f8Ad/zPzs/b6lI8WfDn/sSE/wDT5rNeD/aDjt60UV8Lxn/yUOO/6/Vf/Tkj4vPv+RlX/wAcvzO3+EXii8tYZlilMTaVKi28ik7lVlJ2+m0ZwBjG3jpX1DZXTXVlDKQAZY1cgdASAeKKK/pPwMqzll84ybatH85L8kl6JH6bwDOTw0k30j+pLvo30UV+7n359tfsRylf2Ofh906+IP8A1Kdar0/zz7UUV/E3An/Irl/1+xP/AKk1T8njsHnn2qt4m1ybw18PvFes2whN7omiXN7aedEssazABEdkYFW2l94VgVLKu4MuVJRXq8SNrK69v5Wb0EnUin3Pxj8R+PdU+JvijU/Eet3c+oavrFzJLdXE8ryySMHYcs5LHJ3Ock5eSRurGq0Ux8wdOtFFdcIqMnGOiu/zPOk25tvu/wAz9Rf+Cbhz+wr8Mv8AsCp/6E1FFFdVD+HH0R0rY//Z"
    }
    
    response = client.post(PREFIX + '/users-images', json=json_request_create_user_image)
    
    assert response.status_code == status.HTTP_201_CREATED


def test_update_user_image():
    """Função que testa o endpoint que atualiza uma imagem relacionada à um usuário

    Return: Deve retornar True no caso do status_code ser 204 ou Imagem não encontrada.
    """

    json_request_update_user_image = {
            "user_id": 20,
            "image_id": 15,
            "b64image": "dsfsdfsdfds"
        }
    
    response = client.put('/api/v1/users-images', json=json_request_update_user_image)
    
    if (response.status_code == status.HTTP_204_NO_CONTENT 
        or response.status_code == status.HTTP_404_NOT_FOUND):
        assert True
    else:
        assert False
        

def test_delete_user_image():
    """Função que testa o endpoint que deleta uma imagem relacionada à um usuário

    Return: Deve retornar True no caso do status_code ser 204 ou Imagem não encontrada.
    """
   
    json_delete_user_image = {
        "user_id": 5,
        "image_id": 30
    }
    
    response = client.delete(PREFIX + '/users-images', json=json_delete_user_image)
    
    if (response.status_code == status.HTTP_204_NO_CONTENT 
        or response.status_code == status.HTTP_404_NOT_FOUND):
        assert True
    else:
        assert False


def test_get_user_image_thumb():
    """Função que testa o endpoint que busca imagem relacionada à um usuário e devolve em forma de thumbnail

    Return: Deve retornar true no caso do status_code ser 200 ou 404
    """
    json_get_user_image_thimb = {
        "user_id": 18,
        "image_id": 45
    }
    
    response = client.get(PREFIX + '/users-images-thumbnails', json=json_get_user_image_thimb)
    
    if (response.status_code == status.HTTP_200_OK 
        or response.status_code == status.HTTP_404_NOT_FOUND):
        assert True
    else:
        assert False