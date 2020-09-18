from PIL import Image, ImageDraw, ImageFont

n = 20*2+1
width = 0*2+1
cc = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(cc).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(cc).line((0, n//2, n-1, n//2), fill=0, width=width)

lu = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(lu).line((n//2, n-1, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(lu).line((n//2 - width // 2, n//2, n-1, n//2), fill=0, width=width)

ru = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ru).line((n//2, n-1, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(ru).line((n//2 - width // 2, n//2, 0, n//2), fill=0, width=width)

ld = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ld).line((n//2, 0, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(ld).line((n//2 - width // 2, n//2, n-1, n//2), fill=0, width=width)

rd = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(rd).line((n//2, 0, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(rd).line((n//2 - width // 2, n//2, 0, n//2), fill=0, width=width)

lc = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(lc).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(lc).line((n-1, n//2, n//2, n//2), fill=0, width=width)

rc = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(rc).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(rc).line((0, n//2, n//2, n//2), fill=0, width=width)


ur = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ur).line((n//2, n-1, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(ur).line((0, n//2, n-1, n//2), fill=0, width=width)

dr = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(dr).line((n//2, 0, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(dr).line((0, n//2, n-1, n//2), fill=0, width=width)


ccW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ccW).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(ccW).line((0, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(ccW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

ccB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ccB).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(ccB).line((0, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(ccB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

luW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(luW).line((n//2, n-1, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(luW).line((n//2 - width // 2, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(luW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

luB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(luB).line((n//2, n-1, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(luB).line((n//2 - width // 2, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(luB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

ruW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ruW).line((n//2, n-1, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(ruW).line((n//2 - width // 2, n//2, 0, n//2), fill=0, width=width)
ImageDraw.Draw(ruW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

ruB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ruB).line((n//2, n-1, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(ruB).line((n//2 - width // 2, n//2, 0, n//2), fill=0, width=width)
ImageDraw.Draw(ruB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

ldW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ldW).line((n//2, 0, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(ldW).line((n//2 - width // 2, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(ldW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

ldB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(ldB).line((n//2, 0, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(ldB).line((n//2 - width // 2, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(ldB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

rdW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(rdW).line((n//2, 0, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(rdW).line((n//2 - width // 2, n//2, 0, n//2), fill=0, width=width)
ImageDraw.Draw(rdW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

rdB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(rdB).line((n//2, 0, n//2, n//2 - width//2), fill=0, width=width)
ImageDraw.Draw(rdB).line((n//2 - width // 2, n//2, 0, n//2), fill=0, width=width)
ImageDraw.Draw(rdB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

lcW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(lcW).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(lcW).line((n-1, n//2, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(lcW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

lcB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(lcB).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(lcB).line((n-1, n//2, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(lcB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

rcW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(rcW).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(rcW).line((0, n//2, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(rcW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

rcB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(rcB).line((n//2, n-1, n//2, 0), fill=0, width=width)
ImageDraw.Draw(rcB).line((0, n//2, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(rcB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

urW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(urW).line((n//2, n-1, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(urW).line((0, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(urW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

urB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(urB).line((n//2, n-1, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(urB).line((0, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(urB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)

drW = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(drW).line((n//2, 0, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(drW).line((0, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(drW).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=(255, 255, 255))

drB = Image.new('RGB', (n, n), (255, 232, 98))
ImageDraw.Draw(drB).line((n//2, 0, n//2, n//2), fill=0, width=width)
ImageDraw.Draw(drB).line((0, n//2, n-1, n//2), fill=0, width=width)
ImageDraw.Draw(drB).ellipse((n//4, n//4, n//2+n//4, n//2+n//4), fill=0)


def get_board_img(A):

#    global cc, lu, ru, ld, rd, lc, rc, ur, dr, ccW, luW, ruW, ldW, rdW, lcW, rcW, urW, drW, ccB, luB, ruB, ldB, rdB, lcB, rcB, urB, drB, n

    GO_board = Image.new('RGB', ((40+2)*len(A), (40+3)*len(A)), (255, 232, 98))

    for j in range(len(A)):
        for i in range(len(A[0])):
            elem = A[j][i]
            if elem == 'cc':
                GO_board.paste(cc, (i*40 + len(A), j*40))
            elif elem == 'lu':
                GO_board.paste(lu, (i*40 + len(A), j*40))
            elif elem == 'ru':
                GO_board.paste(ru, (i*40 + len(A), j*40))
            elif elem == 'ld':
                GO_board.paste(ld, (i*40 + len(A), j*40))
            elif elem == 'rd':
                GO_board.paste(rd, (i*40 + len(A), j*40))
            elif elem == 'lc':
                GO_board.paste(lc, (i*40 + len(A), j*40))
            elif elem == 'rc':
                GO_board.paste(rc, (i*40 + len(A), j*40))
            elif elem == 'ur':
                GO_board.paste(ur, (i*40 + len(A), j*40))
            elif elem == 'dr':
                GO_board.paste(dr, (i*40 + len(A), j*40))

            elif elem == 'ccW':
                GO_board.paste(ccW, (i * 40 + len(A), j * 40))
            elif elem == 'ccB':
                GO_board.paste(ccB, (i * 40 + len(A), j * 40))
            elif elem == 'luW':
                GO_board.paste(luW, (i*40 + len(A), j*40))
            elif elem == 'luB':
                GO_board.paste(luB, (i*40 + len(A), j*40))
            elif elem == 'ruW':
                GO_board.paste(ruW, (i*40 + len(A), j*40))
            elif elem == 'ruB':
                GO_board.paste(ruB, (i*40 + len(A), j*40))
            elif elem == 'ldW':
                GO_board.paste(ldW, (i*40 + len(A), j*40))
            elif elem == 'ldB':
                GO_board.paste(ldB, (i*40 + len(A), j*40))
            elif elem == 'rdW':
                GO_board.paste(rdW, (i*40 + len(A), j*40))
            elif elem == 'rdB':
                GO_board.paste(rdB, (i*40 + len(A), j*40))
            elif elem == 'lcW':
                GO_board.paste(lcW, (i*40 + len(A), j*40))
            elif elem == 'lcB':
                GO_board.paste(lcB, (i*40 + len(A), j*40))
            elif elem == 'rcW':
                GO_board.paste(rcW, (i*40 + len(A), j*40))
            elif elem == 'rcB':
                GO_board.paste(rcB, (i*40 + len(A), j*40))
            elif elem == 'urW':
                GO_board.paste(urW, (i*40 + len(A), j*40))
            elif elem == 'urB':
                GO_board.paste(urB, (i*40 + len(A), j*40))
            elif elem == 'drW':
                GO_board.paste(drW, (i*40 + len(A), j*40))
            elif elem == 'drB':
                GO_board.paste(drB, (i*40 + len(A), j*40))
            else:
                pass
#               print(elem, end='')
    const = len(A)
    for i in range(len(A)):
        ImageDraw.Draw(GO_board).text((i*(n-1) + const + n//2 - 5 + (5 if i + 1 < 10 else 0), (n-1)*len(A) - n//2 + 4), str(i+1), fill=0)
        ImageDraw.Draw(GO_board).text((n//2 - 2 + (6 if i + 1 < 10 else 0), (len(A)-i)*(n-1)-n//2-5), str(i+1), fill=0)

#    ImageDraw.Draw(GO_board).text((42*len(A)//3, 41*len(A)), 'fffffff', fill=0)
#            print()
    return GO_board.show()

