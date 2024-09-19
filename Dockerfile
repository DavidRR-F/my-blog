FROM golang:1.23-alpine

ENV HUGO_VERSION 0.134.2

RUN apk add --no-cache git curl && \
    curl -L https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz | tar -xz && \
    mv hugo /usr/local/bin/hugo

RUN adduser -D -u 1001 hugo

WORKDIR /app

RUN chown -R hugo:hugo /app

USER hugo

COPY ./blog .

EXPOSE 1313

CMD ["hugo", "server", "--bind", "0.0.0.0", "--baseURL", "http://localhost", "--buildDrafts", "--watch"]
